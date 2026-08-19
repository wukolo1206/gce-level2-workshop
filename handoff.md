# 工作交接 — 2026-08-18

## 已完成

### 1. Calendar 演練四加入易混淆對照表（@v3.1.1）
- `build_workshop_apps.py` 新增**可選 `practice.table` 欄位**（`caption` / `head` / `rows` / `foot`），
  任一演練都能掛一張對照表，橫向可捲動。這是通用機制，不是為單一演練寫死的。
- Calendar 演練四補上 `+Email 註解指派` vs `@智慧晶片` 的差異表：
  `+` 用在註解框、`@` 用在內文；**未勾選「指派給…」不算指派**；
  並釐清「註解＝批註」與 Slides「演講者備註」是兩回事。

### 2. 公開版考場截圖去識別化（@v3.1.2）— 本次最重要的修補
- 新增 `scripts/mask_exam_screenshot.py`：
  - `actual_exam_screen.png`：模糊第 1 題題幹並覆蓋「（題目內容不公開）」、灰圓遮蔽右上帳號頭像
  - `switch_language_menu.png`：灰圓遮蔽右上帳號頭像
- `build_public_index.py` 這兩張圖改複製 `*_masked.png`（沿用原檔名，HTML 不必改連結），
  **缺打碼檔即 `raise SystemExit` 中止建置**，不會靜默退回原圖。
- 線上 hash 實測確認公開站已換成打碼版。

### 3. 十篇工具講義改採教師工作流順序（@v3.1.3）
- 新順序：`Docs → Slides → Sheets`（做教材）➔ `Classroom → Meet`（開課上課）➔ `Forms`（評量）
  ➔ `Calendar → Gmail`（行政溝通）➔ `Sites`（對外發布）➔ `Practice Sets`（需授權殿後）
- 原順序是「演練數量遞減」，且 Gmail（4 個）誤排在一堆 3 個之後。
- 順序改由 `workshop_content.TOOL_ORDER` **單一來源**決定，`APPS` 與首頁 `TOOLS` 都依它排序，
  並加 `assert` 防兩份清單工具對不上。先前首頁與講義本體各排各的。

### 4. 順手處理的
- 併入前次 session 未提交的 `exam_registration.html`、`build_exam_registration.py`、`workshop_footer.py`。
- Practice Sets 演練一的圖說移除「考題」「Q8」字樣（見「注意事項」第 3 點）。

## 目前進度

三項改動皆已重建、推送兩個 repo，並在 GitHub Pages 線上實測通過
（新順序已生效、打碼圖 hash 相符、11 個公開頁面無破圖）。專案處於可交付狀態。

## 未完成／待確認

- 🔴 **待使用者裁決：是否改寫公開 repo 的 git 歷史。**
  未打碼的原圖自公開 repo commit `cc82fba` 起就已上線一段時間，
  這次替換只換掉**線上檔案**，原圖仍留在 git 歷史中可被取出。
  徹底清除需 `git filter-repo` 移除該 blob 並強制推送（不可逆，已徵詢但尚未執行）。
- `實測檢核表.md` 的 94 項介面核對尚未用真實帳號走過。
- 研習現場試講尚未進行。

## 下一步

1. 決定公開 repo git 歷史要不要清（要清就 `git filter-repo` + force push，只有你一人使用該 repo，風險低但不可逆）。
2. 用真實帳號走 `實測檢核表.md` 的 94 項介面核對，Google UI 文案改版頻繁，這是現場最容易當場破功的地方。
3. 研習現場試講。

## 注意事項

1. **兩個 repo、兩次 push**
   - 本資料夾本身是獨立 repo（私人版 `gce-level2-workshop-private`），**不是** `D:\備課ai` 那個大 repo，
     所以在這個資料夾內用 `git add -A` 是安全的、只會掃到本專案。
   - 公開版輸出在 `C:\repos\gce-level2-workshop`（Drive 同步範圍外），要另外 commit + push。
   - 標準流程：改 `scripts/workshop_content.py` ➔ `build_workshop_apps.py` ➔
     `build_course_structure_map.py` ➔ `build_public_index.py` ➔ 兩邊各 push 一次。

2. **公開版白名單只擋檔名，不看圖片內容**
   這次的外洩就是這樣發生的：加圖時只確認「頁面需要這張圖」，沒有開圖看內容。
   任何截圖進 `ALLOWED` 清單前，**實際開圖看過像素**，重點查兩類：可讀的官方題幹、帳號頭像／Email／姓名。
   已寫入 PITFALLS。

3. **有另一個 session 同時在改這批檔案**
   本次重建撈到別的 session 正在進行的 Practice Sets 改版（三張實機圖 + 改寫步驟）。
   三張圖檢查過是乾淨的空白介面，白名單他們也加好了；但圖說有「考題」「Q8」字樣，
   會破壞學員版零考試痕跡，我改成講「官方英文名稱 Extra help vs 介面中文『資源』」的中英落差。
   **若那個 session 對措辭另有打算，回頭改 `workshop_content.py` 第 1131-1141 行。**
   下次動這批檔案前先 `git status` 看有沒有別人的 in-flight 變更。

4. **學員版零考試痕跡是硬規則**（v3.1.0 訂下）
   公開版不可出現「考題」「Q 題號」「Lab 編號」「應考」等字樣。
   掃描時 `Q[0-9]` 會誤中 Google 檔案 ID，`考試大綱`／`報名流程與考試架構` 是報名頁的合法用語，需人工判讀。

5. **Meet 串流直播需付費授權**
   Live stream 需 Education Plus 或 Teaching and Learning Upgrade，個人 Gmail 與 Education Fundamentals 都看不到該選項。
   這點只寫在 PITFALLS，**兩份 Lab 講義（`GCE_Level_2_Lab_2_Calendar_實作題完整指南.md` Task 2、
   `GCE_Level_2_Lab_Exams_15個實務操作練習題庫與學習手冊.md` 演練 2-2）仍直接叫人「點選新增串流」，
   授權門檻註記尚未補進去**——研習現場學員照做會全體卡住。已向使用者提出，尚未動工。
