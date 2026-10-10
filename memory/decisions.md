# 決定ログ

追記のみ。形式：`[日付] (著者) 決定内容 (理由)`

- [2026-10-10] (user+Qwen) 外部記憶を Notion から .md ファイルベースに移行 (Notion で約1年運用してきたが、AI が直接ファイルの読み書きができる時代になり、Web版Claude もファイル添付対応したため)
- [2026-10-10] (user+Qwen) 同期は git（GitHub非公開）を正体、Google Drive を Windows への運搬役 (履歴が残る・無料・AI運用と統合できる / Drive は競合リスクがあるため写し役だけにする)
- [2026-10-10] (user+Qwen) Windows は Obsidian（閲覧）＋Claude のみ。ローカルLLM は置かない (PC が非力で、Claude はクラウド推論なので性能不問)
- [2026-10-10] (Qwen) Mac での vault 置き場所は ~/Documents/ai-vault (アプリ管理下に置かず、安定したユーザー所有フォルダにする)
- [2026-10-10] (user+Qwen) 作業順変更：新しいMac（M5 Max）を購入した直後なので、まず古いMac（M1 Max）からのデータ移行を完了させる (移行完了まで vault 本格運用・Agent Team 再設計は保留)
- [2026-10-10] (user+Qwen) 移行後に Claude Agent Team V1.3（8 Projects ＋ Notionタスクバス ＋ Cowork）を再設計。Notion の役割も再検討 (アジェンダは projects/agent-team-redesign.md)
- [2026-10-10] (Qwen) 機密データには `confidential/` ディレクトリ（gitignore＝ローカルのみ）を導入。vault は個人端末限定、社内EDR端末には置かない
