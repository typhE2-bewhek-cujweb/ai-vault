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

## ファイルマップ

| ファイル | 中身 |
|---|---|
| `MEMORY.md` | 入口：現在の目標・次の手・重要決定（短く保つ） |
| `memory/INDEX.md` | 記憶ファイルのガイド |
| `memory/goals.md` | 長期目標・方針 |
| `memory/decisions.md` | 決定ログ（日付＋著者＋理由、追記のみ） |
| `memory/journal.md` | 作業手記（最近） |
| `projects/` | プロジェクト別の状態ファイル |
