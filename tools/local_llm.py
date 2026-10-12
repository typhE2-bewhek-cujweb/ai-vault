#!/usr/bin/env python3
"""ローカルLLM（LM Studio）呼び出しツール。

ai-vault の前提情報（共通指示・用語集・共有メモリ）を自動でシステムプロンプトに付けて、
LM Studio の OpenAI 互換 API に送る。標準ライブラリのみで動く。

使い方:
  python3 tools/local_llm.py "質問文"
  python3 tools/local_llm.py -m japanese -f 入力ファイル.txt "この文書を要約して"
  echo "本文" | python3 tools/local_llm.py -m reasoning "次の文章の論点を整理して"
  python3 tools/local_llm.py --list          # 使えるモデルの一覧
  python3 tools/local_llm.py --no-context "前提情報なしで質問"

オプション:
  -m / --model    用途名（reasoning/japanese/general/vision/granite/qwen）またはモデルID
  -f / --file     入力として添付するテキストファイル（複数可）
  -e / --effort   推論の深さ low/medium/high（gpt-oss など対応モデルのみ）
  --max-tokens    出力の上限（既定 4000）
  --json          応答の全情報を JSON で出力
  --where         どの接続先につながるかだけを表示
  --warmup        config の warmup に挙げたモデル（既定：reasoning・japanese）を先に読み込む
  --print-context 前提情報（システムプロンプト）を表示。LM Studio のプリセット登録用
                  例: python3 tools/local_llm.py --print-context | pbcopy

接続先: config/local_llm.json の hosts を順に試す（Mac名 → Mac自身 → 予備アドレス）。
オフライン（ネットなし）でも Mac 上で実行すれば 127.0.0.1 で動く。
"""
import argparse, json, os, sys, time, urllib.request, urllib.error

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


STATE = os.path.join(VAULT, ".state", "local_llm_last.json")


def load_config():
    with open(os.path.join(VAULT, "config", "local_llm.json"), encoding="utf-8") as f:
        cfg = json.load(f)
    return cfg


def _probe(url, token, timeout):
    req = urllib.request.Request(url + "/models")
    req.add_header("Authorization", "Bearer " + token)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status == 200
    except Exception:
        return False


def resolve_base_url(cfg):
    """接続先を決める。環境変数 > 前回の接続先 > hosts の順に試す。"""
    env = os.environ.get("LOCAL_LLM_BASE_URL")
    if env:
        return env.rstrip("/")
    token = read_token(cfg)
    port = cfg.get("port", 1234)
    cands = []
    try:
        with open(STATE, encoding="utf-8") as f:
            cands.append(json.load(f)["base_url"])
    except Exception:
        pass
    for h in cfg.get("hosts", []):
        u = f"http://{h}:{port}/v1"
        if u not in cands:
            cands.append(u)
    tried = []
    for u in cands:
        tried.append(u)
        if _probe(u, token, cfg.get("probe_timeout_sec", 3)):
            os.makedirs(os.path.dirname(STATE), exist_ok=True)
            with open(STATE, "w", encoding="utf-8") as f:
                json.dump({"base_url": u, "time": time.strftime("%Y-%m-%d %H:%M:%S")}, f)
            return u
    sys.exit("[エラー] LM Studio に接続できません。試した接続先:\n  " + "\n  ".join(tried) +
             "\nMac が起動中か、LM Studio のサーバーが Running か、「ローカルネットワークで提供」がオンか確認してください。")


def read_token(cfg):
    path = os.path.join(VAULT, cfg["token_file"])
    try:
        with open(path, encoding="utf-8") as f:
            tok = f.read().strip()
    except FileNotFoundError:
        sys.exit(f"[エラー] 認証の鍵ファイルがありません: {path}")
    if tok.startswith("{\\rtf"):
        sys.exit("[エラー] 鍵ファイルがリッチテキスト形式です。標準テキストで保存し直してください。")
    return tok


def request(cfg, path, payload=None):
    if "base_url" not in cfg:
        cfg["base_url"] = resolve_base_url(cfg)
    url = cfg["base_url"] + path
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(url, data=data, method="POST" if data else "GET")
    req.add_header("Authorization", "Bearer " + read_token(cfg))
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=cfg.get("timeout_sec", 170)) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")[:500]
        sys.exit(f"[エラー] HTTP {e.code}: {body}")
    except (urllib.error.URLError, TimeoutError) as e:
        sys.exit(f"[エラー] LM Studio との通信に失敗しました（{cfg['base_url']}）: {e}")


def build_context(cfg):
    parts = []
    for rel in cfg.get("context_files", []):
        p = os.path.join(VAULT, rel)
        if os.path.exists(p):
            with open(p, encoding="utf-8") as f:
                parts.append(f"<!-- {rel} -->\n" + f.read().strip())
    return "\n\n".join(parts)


def main():
    ap = argparse.ArgumentParser(description="LM Studio 呼び出し（ai-vault の前提情報付き）")
    ap.add_argument("prompt", nargs="?", default="")
    ap.add_argument("-m", "--model")
    ap.add_argument("-f", "--file", action="append", default=[])
    ap.add_argument("-e", "--effort")
    ap.add_argument("--max-tokens", type=int, default=4000)
    ap.add_argument("--no-context", action="store_true")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--where", action="store_true")
    ap.add_argument("--print-context", action="store_true")
    ap.add_argument("--warmup", action="store_true")
    a = ap.parse_args()
    cfg = load_config()

    if a.warmup:
        for key in cfg.get("warmup", []):
            mid = cfg["models"].get(key, key)
            t0 = time.time()
            request(cfg, "/chat/completions",
                    {"model": mid, "messages": [{"role": "user", "content": "ok"}], "max_tokens": 1})
            print(f"{mid}: 読み込み済み（{time.time()-t0:.1f}秒）")
        return

    if a.print_context:
        print(build_context(cfg))
        return

    if a.where:
        print(resolve_base_url(cfg))
        return

    if a.list:
        ids = [m["id"] for m in request(cfg, "/models").get("data", [])]
        alias = {v: k for k, v in cfg["models"].items()}
        for i in ids:
            print(f"{i}" + (f"  （用途名: {alias[i]}）" if i in alias else ""))
        return

    user = a.prompt
    for fp in a.file:
        with open(fp, encoding="utf-8", errors="replace") as f:
            user += f"\n\n--- 添付: {os.path.basename(fp)} ---\n" + f.read()
    if not sys.stdin.isatty():
        piped = sys.stdin.read()
        if piped.strip():
            user += "\n\n--- 入力 ---\n" + piped
    if not user.strip():
        sys.exit("[エラー] 依頼内容が空です。")

    key = a.model or cfg["default_model"]
    model = cfg["models"].get(key, key)
    messages = []
    if not a.no_context:
        messages.append({"role": "system", "content": build_context(cfg)})
    messages.append({"role": "user", "content": user})
    payload = {"model": model, "messages": messages, "max_tokens": a.max_tokens}
    effort = a.effort or (cfg.get("default_reasoning_effort") if "gpt-oss" in model else None)
    if effort:
        payload["reasoning_effort"] = effort

    t0 = time.time()
    res = request(cfg, "/chat/completions", payload)
    dt = time.time() - t0
    if a.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return
    msg = res["choices"][0]["message"]
    print((msg.get("content") or "").strip())
    u = res.get("usage", {})
    print(f"\n[{cfg['base_url']} / model={model} / {dt:.1f}秒 / 入力{u.get('prompt_tokens','?')}・出力{u.get('completion_tokens','?')}トークン]",
          file=sys.stderr)


if __name__ == "__main__":
    main()
