# Claude Agent Team 再設計

ステータス: プランニング（M1 Max → M5 Max 移行の完了後に着手）
ソース: 全体設計書 V1.3（2026-03, CONFIDENTIAL — 全文は `confidential/`）

## 現行アーキテクチャ（V1.3）
- Claude Projects 8エージェント：司令塔 ＋ 秘書(待機) ＋ 業務管理(メイン窓口) ＋ 渉外・文書 ＋ チーム統括 ＋ 技術統括 ＋ 委託先PM ＋ 事業戦略
- Notion Secretary Hub ＝ Agent間タスクバス（擬似連携：書き込み→起動時読み取り→完了処理）
- Cowork（Claude Desktop）＝ ローカルファイル生成（Excel/Word/PPT）＋ GD→OneDrive デュアルストレージミラー ＋ スケジュールタスク
- MCP 7接続（Gmail / Drive / Calendar / Slack / Figma / Notion / Mermaid）
- デュアルストレージ：GD（個人ドメイン）がプライマリ、OneDrive（社内）は最終成果物のみ
- プラン：Claude Pro（M365コネクター不可など制約あり）

## 再設計アジェンダ（TBD）
1. **Notionタスクバスの再検討** — ファイルベース（vault/git）へ置換できるか、2026年のClaude新原語でより良い構造があるか
2. **8 Projects の構造再検討** — 統合・Skill化・役割再分担
3. **ローカルQwenの位置づけ** — 機密ワーク（社内・人事関連）をローカル限定ループで回す？
4. **Cowork のスケジュール・デュアルストレージ方針再検討**
5. **セキュリティ境界** — confidential/ パターン、vault は個人端末限定
6. **vault を Agent Team 全体の共有記憶としてどう組み込むか**（Notion の一部を補完・代替）

## 制約（維持）
- デュアルドメインのメール送信ルール、敬称ルール、OneDriveは最終成果物のみ
- 個人（チームメンバー）に関する情報は `confidential/` 外に出さない
