# CLAUDE.md — 全AI共通ルール

このフォルダ（ai-vault）は複数AIが読み書きする共有メモリです。
- Claude（このCLI）
- ローカルQwen（Macの LM Studio Bionic）

## ルール（必ず守る）

1. 作業開始時、まず `MEMORY.md` を読む。次に `memory/` の関連ファイルを読む。
2. 作業終了時、必ず書き戻す：
   - 決まったこと → `memory/decisions.md`（追記）
   - やったこと → `memory/journal.md`（「最近」へ追記）
   - 目標・次の手が変わったら → `MEMORY.md` 更新
3. 履歴を削除しない。修正は新しいエントリで上書き説明する。
4. ファイルが約200行を超えたら、古い内容を要約に圧縮する（要点だけ残す）。
5. 日本語、標準Markdownで記述する（frontmatter 可）。
6. 変更後は `git add -A && git commit`。push はユーザーに明示された時だけ。
7. セキュリティ：この vault は個人端末専用。社内 EDR 保護端末に clone・配置しない。`confidential/` はローカルのみ（gitignore）で、その中身を共有ファイルへ載せない。

## ファイルマップ

| ファイル | 中身 |
|---|---|
| `MEMORY.md` | 入口：現在の目標・次の手・重要決定（短く保つ） |
| `memory/INDEX.md` | 記憶ファイルのガイド |
| `memory/goals.md` | 長期目標・方針 |
| `memory/decisions.md` | 決定ログ（日付＋著者＋理由、追記のみ） |
| `memory/journal.md` | 作業手記（最近） |
| `projects/` | プロジェクト別の状態ファイル |
| `memory/glossary.md` | 用語集（ローカルLLMの取り違え防止） |
| `config/local_llm.json` | ローカルLLMの接続設定 |
| `tools/local_llm.py` | ローカルLLM呼び出しツール |
| `prompts/local_system.md` | ローカルLLM用の共通指示 |
| `offline/` | オフライン作業の成果物と作業メモ（復帰時に Claude が引き継ぐ） |

## ローカルLLM（LM Studio）への依頼

Claude は `tools/local_llm.py` で Mac 本体の LM Studio に処理を依頼できる。前提情報（`prompts/local_system.md`・`memory/glossary.md`・`MEMORY.md`）は自動で付く。

| 用途名 | モデル | 使う場面 |
|---|---|---|
| reasoning（既定） | gpt-oss-120b | 推論・分析・英文読解。速い |
| japanese | llm-jp-4.1-32b-a3b-thinking | 日本語の文書下書き |
| general | google/gemma-4-31b | 汎用・長文 |
| vision | nvidia/nemotron-3-nano-omni | 画像・文書の読み取り |

ローカルに任せる基準：大量の繰り返し処理、Mac 内のファイルの一括処理、オフラインでの作業、比較・検証。
判断・仕上げ・外部サービス連携は Claude が行う。

```
python3 tools/local_llm.py "依頼文"
python3 tools/local_llm.py -m japanese -f 入力.txt "要約して"
python3 tools/local_llm.py --list
```

- 接続先は `config/local_llm.json` の `hosts` を順に試す（Mac名 `KENs-MBP165.local` → `127.0.0.1` → 予備アドレス）。最後の接続先は `.state/`（git 対象外）に記録される。`--where` で確認できる
- 認証の鍵は `confidential/lmstudio_token.txt`（git 対象外）。鍵の文字列をチャットや共有ファイルに書かない
- 用語の取り違えがあれば `memory/glossary.md` に追記する

## オフライン作業と引き継ぎ

Mac はノートで、移動中はネットに接続できないことがある。オフラインの間は Claude が使えないため、LM Studio（ローカル）だけで作業し、成果を `offline/` に残す。

- オフライン時：作業メモ `offline/YYYYMMDD_件名.md`（ひな形 `offline/_TEMPLATE.md`）と成果物を置く
- **Claude は作業開始時、`offline/` に「状態: 未引き継ぎ」のメモがあれば最初に確認し、ユーザーに報告する**
- 引き継ぎ時：未完了の項目を処理（仕上げ・外部送付など）し、決定は `memory/decisions.md`、作業は `memory/journal.md` に反映。メモの状態を「引き継ぎ済み」に変える（削除しない）
- LM Studio のチャット用プリセットは `python3 tools/local_llm.py --print-context` の出力をシステムプロンプトに貼って作る。共通指示・用語集を更新したら貼り直す

