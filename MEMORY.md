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
- [ ] **Notion のエクスポート**を `notion-export/` に置く → 統合・圧縮して memory/ へ（手順: notion-export/README.md）
- [ ] Mac: node 導入 → Claude Code（手順: docs/macos-claude-code.md）
- [ ] Windows: docs/windows-setup.md に従う（Drive 内に clone ＋ Obsidian ＋ obsidian-git）
- [ ] 同期フロー実機検証（Mac で編集 → Windows に反映されるか）

## 使い方
このファイルを読んでから、`memory/INDEX.md` を見て必要なファイルを読む。
