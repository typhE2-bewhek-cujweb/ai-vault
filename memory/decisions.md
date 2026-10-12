# 決定ログ

追記のみ。形式：`[日付] (著者) 決定内容 (理由)`

- [2026-10-10] (user+Qwen) 外部記憶を Notion から .md ファイルベースに移行 (Notion で約1年運用してきたが、AI が直接ファイルの読み書きができる時代になり、Web版Claude もファイル添付対応したため)
- [2026-10-10] (user+Qwen) 同期は git（GitHub非公開）を正体、Google Drive を Windows への運搬役 (履歴が残る・無料・AI運用と統合できる / Drive は競合リスクがあるため写し役だけにする)
- [2026-10-10] (user+Qwen) Windows は Obsidian（閲覧）＋Claude のみ。ローカルLLM は置かない (PC が非力で、Claude はクラウド推論なので性能不問)
- [2026-10-10] (Qwen) Mac での vault 置き場所は ~/Documents/ai-vault (アプリ管理下に置かず、安定したユーザー所有フォルダにする)
- [2026-10-10] (user+Qwen) 作業順変更：新しいMac（M5 Max）を購入した直後なので、まず古いMac（M1 Max）からのデータ移行を完了させる (移行完了まで vault 本格運用・Agent Team 再設計は保留)
- [2026-10-10] (user+Qwen) 移行後に Claude Agent Team V1.3（8 Projects ＋ Notionタスクバス ＋ Cowork）を再設計。Notion の役割も再検討 (アジェンダは projects/agent-team-redesign.md)
- [2026-10-10] (Qwen) 機密データには `confidential/` ディレクトリ（gitignore＝ローカルのみ）を導入。vault は個人端末限定、社内EDR端末には置かない
- [2026-10-12] (user+Claude) Mac での vault 置き場所を ~/ai-vault（ホーム直下）に変更。2026-10-10 の「~/Documents/ai-vault」を置き換え (~/Documents は iCloud「デスクトップと書類」同期の対象で、confidential/ の鍵が iCloud に上がること・.git が同期で壊れる恐れがあるため)
- [2026-10-12] (user+Claude) Claude（Cowork）から LM Studio サーバーへ LAN 経由で直接接続する方式を採用。認証トークン必須、トークンは confidential/lmstudio_token.txt に保存 (取り次ぎプログラム不要で、依頼と結果回収を直接行えるため)
- [2026-10-12] (user+Claude) LM Studio の接続先は IP 固定でなく Mac 名（KENs-MBP165.local）を優先し、つながらなければ 127.0.0.1・予備アドレスを順に試す (Mac はノートで移動が多く、ネットワークごとに IP が変わるため)
- [2026-10-12] (user) 公共 Wi-Fi でも LM Studio の「ローカルネットワークで提供」はオンのまま運用し、認証トークンで保護する（案B） (切り替えの手間を避けるため。危険度がやや上がることは了承済み)
- [2026-10-12] (user+Claude) オフライン作業は offline/ に作業メモと成果物を残し、オンライン復帰時に Claude が引き継ぐ (移動中に LM Studio だけで作業できるようにするため)
