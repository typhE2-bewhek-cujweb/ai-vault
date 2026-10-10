# MEMORY.md — 共有メモリの入口

_最終更新: 2026-10-10 (Qwen/Bionic) — 骨格作成_

## 現在の目標
- Claude と Qwen を並行利用し、共有記憶で運用する体制を完成させる。

## 重要決定（要約）
- 外部記憶は Notion からファイル（.md）ベースに移行
- 同期は git（GitHub非公開）を正体、Google Drive を Windows への運搬役
- Windows は閲覧＋Claude のみ（ローカルLLMは置かない）
- 詳細は `memory/decisions.md` を参照

## 次の手
1. [ ] **旧Mac（M1 Max）→ 新Mac（M5 Max）へのデータ移行** — 最優先。完了後に以下へ
2. [ ] Agent Team 再設計（→ projects/agent-team-redesign.md）
3. [ ] Notion エクスポート → notion-export/（クラウドなので移行と並行可）
4. [ ] Mac: node → Claude Code（docs/macos-claude-code.md）
5. [ ] Windows: docs/windows-setup.md ＋ 同期フロー実機検証

## 使い方
このファイルを読んでから、`memory/INDEX.md` を見て必要なファイルを読む。
