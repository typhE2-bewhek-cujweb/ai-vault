# Windows セットアップ手順書（ai-vault）

目的：Windows PC で Obsidian により vault を閲覧し、更新を受け取る。
原則：**Mac が主編集側**（Qwen + Claude Code）。Windows は受信＋時々 Claude で作業。

## 0. ゴールデンルール
**2台で同時に作業しない。** Windows で作業始める前に pull する（下記で自動化される）。

## 1. Git for Windows をインストール
1. https://git-scm.com/download/win からダウンロード→そのままインストール（全部デフォルトでOK）
2. 完了後、ターミナル系のアプリは**一旦閉じてから開き直す**

## 2. Google Drive の同期フォルダ内に clone
1. エクスプローラーで Google Drive の同期フォルダを開く（通常 `C:\Users\<ユーザー名>\Drive`）
2. アドレス欄に `cmd` と打って Enter（コマンドプロンプトが開く）
3. 実行：
   ```
   cd C:\Users\<ユーザー名>\Drive
   git clone https://github.com/typhE2-bewhek-cujweb/ai-vault.git
   ```
   → `ai-vault` フォルダが Drive に現れる
4. 初回認証：Username に `typhE2-bewhek-cujweb`、Password に**トークン**を貼り付け
   （Mac と同じ作り方で、Fine-grained → Repository access: ai-vault → Contents: Read and write）
   → Windows の Credential Manager に保存され、以降は自動

## 3. Obsidian をインストール
1. https://obsidian.md からインストール
2. **Open folder as vault** → `C:\Users\<ユーザー名>\Drive\ai-vault` を選択
3. Mac と同じファイルが見えれば ✅

## 4. obsidian-git プラグイン（更新を自動化）
1. Settings → Community plugins → **Turn on community plugins**
2. Browse → `obsidian-git` で検索 → Install → **Enable**
3. obsidian-git の設定：
   - **Auto pull on startup: ON**
   - **Auto pull interval: 30m**
   - **Auto push on file change: ON（間隔 10m でOK）**
4. 以後は Obsidian を開くだけで最新化。**git コマンドは不要**
   （手動: `Ctrl+P` → "obsidian-git: Pull" / "Push"）

## 5. Claude Code を Windows で使う場合
（node のインストールが必要：https://nodejs.org から Windows 版）
```
npm install -g @anthropic-ai/claude-code
cd C:\Users\<ユーザー名>\Drive\ai-vault
claude
```
vault 内なら CLAUDE.md を自動で読み、メモリルールに従って動く。

## トラブルシュート
- **pull が失敗する** → "obsidian-git: Pull" を手動実行してエラーを見る（共通原因：2台同時編集）
- **ファイルが Drive で「クラウドのみ」表示** → 右クリック「このデバイスに常時保存」
- **衝突ファイル（`- Copy` 等）が出た** → 内容を比較し古い方を削除→Push
