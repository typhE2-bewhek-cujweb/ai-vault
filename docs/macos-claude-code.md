# Claude Code 導入手順書（Mac）

## 1. Node のインストール（要：Claude Code のランタイム）

### 方式A：公式インストーラ（一番簡単・推奨）
1. https://nodejs.org → macOS インスローラ（LTS / .pkg）をダウンロード→インストール
2. **ターミナルを閉じてから開き直す**
3. 確認：`node --version`（v20 以上ならOK）

### 方式B：Homebrew（長期的には最強だが導入が重い）
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
（Mac のパスワードを要求される。指示通り PATH に追加）
その後 `brew install node`

## 2. Claude Code のインストール
```
npm install -g @anthropic-ai/claude-code
```

## 3. 初回ログイン
```
cd ~/Documents/ai-vault
claude
```
1. ログイン方式を選択 → ブラウザで Claude アカウントにログイン（Max サブスクがあればそのまま）
2. vault 内なら **CLAUDE.md を自動読み** → メモリルール（MEMORY.md の読書・書き戻し）がそのまま適用される

## 4. 動作確認
claude に：
> 「まず MEMORY.md を読んで、現在の目標と次の手を教えて」

中身が正しく返れば接続成功 ✅

## 5. 日常の使い方
- 作業したいフォルダで `claude` を起動
- 作業終了時に MEMORY.md / journal の更新を頼む（CLAUDE.md で指示済みだが、明示してもOK）
- git push は私（Bionic/Qwen）が代行する運用
