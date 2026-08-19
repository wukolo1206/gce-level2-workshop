# CHANGELOG.md

## @v3.1.3 — 2026-08-17
- **十篇工具講義改採教師工作流順序**（已部署，線上實測確認）：
  做教材 `Docs → Slides → Sheets` ➔ 開課上課 `Classroom → Meet` ➔ 評量 `Forms`
  ➔ 行政溝通 `Calendar → Gmail` ➔ 對外發布 `Sites` ➔ 加值 `Practice Sets`（需授權殿後）。
  原順序為「演練數量遞減」，且 Gmail（4 個）誤排在一堆 3 個之後。
- 順序改由 `workshop_content.TOOL_ORDER` **單一來源**決定，`APPS` 與首頁 `TOOLS` 都依它排序，
  並加 `assert` 防兩份清單工具不一致；先前首頁與講義本體各排各的。
- Practice Sets 演練一補上三張實機介面對照圖（「資源」＝Extra help 的中英文落差），
  圖說措辭移除「考題」「Q8」，維持學員版零考試痕跡。

## @v3.1.2 — 2026-08-17
- **公開版考場截圖全面去識別化**（已部署，線上 hash 實測確認）：
  新增 `scripts/mask_exam_screenshot.py`，`actual_exam_screen.png` 模糊第 1 題題幹並覆蓋
  「題目內容不公開」、遮蔽右上帳號頭像；`switch_language_menu.png` 遮蔽帳號頭像。
- `build_public_index.py` 這兩張圖改複製 `*_masked.png`（沿用原檔名），
  **缺打碼檔即中止建置**，不會靜默退回原圖。
- 併入前次 session 未提交的 `exam_registration.html`、`build_exam_registration.py`、`workshop_footer.py`。
- ⚠️ **未打碼原圖自 `cc82fba` 起已公開約一段時間，且仍留在公開 repo 的 git 歷史中**，
  詳見 PITFALLS「公開版夾帶真實考題截圖與帳號頭像」。

## @v3.1.1 — 2026-08-17
- `build_workshop_apps.py` 演練區塊新增**可選 `practice.table` 欄位**（`caption` / `head` / `rows` / `foot`），
  可在任一演練下方掛一張易混淆對照表，橫向可捲動。
- **Calendar 演練四**加入 `+Email 註解指派` 與 `@智慧晶片` 的差異對照表：
  釐清 `+` 用在註解框、`@` 用在內文；點明**未勾選「指派給…」不算指派**；
  並註明「註解＝批註」與 Slides「演講者備註」是兩回事。
- 註腳措辭避開「考試／考題」用語，維持 v3.1.0 訂下的學員版零考試痕跡（重建後掃描為 0）。

## @v3.1.0 — 2026-08-17
- **上線 GitHub Pages**：<https://wukolo1206.github.io/gce-level2-workshop/>（已實測 HTTP 200）。
- **建立兩個 repo**：公開版 `gce-level2-workshop`（18 檔，僅學員版內容）與私人版 `gce-level2-workshop-private`（完整工作檔）。
- 新增 `scripts/build_public_index.py`：產生公開版精簡首頁並以白名單方式打包，
  自動把「回研習主講義」改寫為「回講義首頁」；輸出到 `C:\repos\gce-level2-workshop`（Drive 同步範圍外）。
- **公開版排除**官方題庫、Lab 實作題指南、考場實景截圖、講師版對照表與 `study_guide_app.html`；
  掃描確認零考題痕跡、零死連結、零缺圖。
- 學員端側邊欄新增「🔗 官方課程」區：繁中版課程、英文版課程、Teacher Center、18 個 Lessons 逐課連結。
- **移除學員端所有考試痕跡**：卡片的「含官方實作題 Lab N」標記、術語表 32 條備註中的 Q 題號與 Lab 編號、
  圖例的「選擇題考過／Lab 自動評分」改為「核心功能／名稱須完全一致／容易混淆」，
  以及散在演練中的「考題會考」「應考練習」等字樣。十篇工具講義掃描零殘留。

## @v3.0.0 — 2026-08-16
- **導覽改版：以工具為主軸**。主講義預設分頁改為「🧰 十篇工具講義」十宮格；側邊欄由 31 項精簡為 10 篇工具（單一清單、不分級）＋課程結構對照＋下載 Word；
  6 個 Unit 章節導覽改為僅在「完整版研習講義」檢視時顯示。
- **新增課程結構三方對照** `course_structure_map.html`：官方繁中 11 個實務單元 × 英文 6 Units × 10 篇工具講義，
  解決「兩個語言版本目錄完全不同」的困惑；保留 Unit 作為「綜合應用情境」視角（一個情境要串哪幾個工具）。
- **內部連結全部改為同分頁**（55 條）；Google 雲端檔案與官方課程維持另開分頁。
- **備考工具移出學員端**：25 題刷題、25 個實作演練、3 個官方實作題 Lab 移到講師版 `instructor_coverage_map.html`。
- **新增中英術語對照表**：10 篇工具講義各附一張（共 80 組），標示 ★ 選擇題考過、⚙ Lab 自動評分逐字比對、⚠️ 常見誘答。
- **兩輪外部 AI 交叉審查（Codex）**，共 41 條回饋，採納 39、部分採納 2：
  - 第一輪 27 條：修正 9 處介面名稱（主題製作工具、資料欄統計資料、建立篩選器檢視畫面、根據答案前往相關區段、回覆分頁、
    新增作答意見回饋、使用電話收發音訊／撥入、預訂頁面複製連結、資源→新增練習題）、7 處步驟邏輯錯誤、3 處現場前提
    （Gmail 代理 24 小時生效、Meet 撥入需同網域、Sites 公開可能被管理員關閉）。
  - 第二輪 14 條：抓到第一輪改動引入的三個新錯誤（Classroom 公告步驟改到一半、回應驗證被誤改為回覆驗證、
    成績匯入同網域條件寫錯），另修正課程深入分析、安排時間、供所有學生瀏覽等名稱。
  - 部分採納：Mote（保留 Marketplace 考點＋補 Chrome 擴充功能實際安裝路徑）、@People/@Date（保留考點名稱＋改用實際操作寫法）。
- 新增 `scripts/build_review_package.py`（審查包產生器）與 `實測檢核表.md`（94 項介面名稱／路徑的人工實測清單）。
- 第二批 25 個範本檔（hands_on_tasks_app 使用）的公開權限亦由 writer 降為 reader；全站 `/edit` 連結歸零
  （51 條 `/copy`＋65 條 `/preview`）。兩個範本檔更名以配合新術語。

## @v2.9.0 — 2026-08-16
- **考點全覆蓋**：盤點 25 題選擇題與 3 個實作題（15 Task）對現有演練的覆蓋率，補上 4 個新演練 + 3 處微調後達成 **25/25 題、15/15 Task 全覆蓋**（演練總數 36 ➔ 40）。
  - Calendar 新增**演練五 系列活動與活動素材**（重複活動、夾帶檔案、新增地點）➔ 收 Q01 與 Lab2 T1/T3。
  - Classroom 新增**演練五 班級公告**（附加檔案、指定對象、排定發布）➔ 收 Lab1 T5，並釐清「公告 vs 作業」的判斷。
  - Slides 新增**演練四 分享權限層級**（檢視者／註解者／編輯者，送審一律用註解者）➔ 收 Lab3 T5 這個官方標註的失分點。
  - Docs 新增**演練七 表格＋超連結探索學習單**（外部網址／雲端檔案／書籤三種連結目標）➔ 收 Q13。
  - 微調：Slides 演練一補「插入選單／右鍵」兩種連結路徑與外部資源（Q18）；演練二補預留位置須精確命名（Lab3 T2 自動評分逐字比對）；演練三補 Drive 影片分頁（Lab3 T4）。
- **串流直播三種帳號實測結果寫入講義**：個人 Gmail 只有齒輪無展開箭頭（上限 100 人）；Education Fundamentals 有箭頭但展開只有會議代碼；Education Plus / T&L 才有「新增串流直播」。
  並提醒：官方 Lab 2 Task 2 直接要求設定串流直播，報考需用有授權的帳號。
- **新增講師版覆蓋對照表** `instructor_coverage_map.html`（`scripts/build_instructor_map.py` 產生）：
  25 題與 15 個 Lab Task 的逐項對應、各項帳號門檻、三種帳號能力對照表。
  刻意不從學員端連結，學員端維持「情境 ➔ 功能 ➔ 實作」不顯示考題編號。

## @v2.8.1 — 2026-08-16
- 修正 Calendar 演練四按鈕名稱錯誤：「新增會議紀錄 (Add meeting notes)」➔「**建立會議記錄** (Create meeting notes)」，
  並標明它是<說明欄工具列最左邊的 Google 文件圖示>而非文字連結（依 support.google.com/docs/answer/11324079 查證）；Docs 篇演練六同步修正。
- 依實際 zh-TW 介面修正演練三用語：與會者權限 ➔ **邀請對象權限**、邀請他人 ➔ **邀請其他使用者**、查看與會者名單 ➔ **查看邀請對象名單**，
  並補註這兩項預設為已勾選、通知欄位需進「更多選項」完整編輯頁。
- Calendar 演練二新增授權門檻提醒：**串流直播需 Education Plus / Teaching and Learning Upgrade**（與 Practice Sets 同級），
  一般帳號看不到該選項，附替代作法與考點說明。
- 新增 `scripts/verify_calendar_ui.py`（唯讀 UI 驗證工具，需人工登入後自動比對按鈕名稱並截圖）。

## @v2.8.0 — 2026-08-16
- **範本檔權限收斂**：以 Drive API 將 25 個範本檔的 `anyone` 權限由 **writer 降為 reader**（原狀態存於 `permissions_snapshot_before_reader.json` 可還原）；
  複查確認 25/25 為 reader 且未鎖複製，`/copy` 仍正常。
- **觀摩型連結改為 `/preview` 唯讀**：各 App 底部的「情境補充說明文件」共 23 處，避免有人誤入編輯模式。
- **新增 Gmail 工具篇** `gmail_workshop_app.html`（4 個演練）：帳戶代理授權（兩人一組互相授權，含同網域限制提醒）、
  篩選器與標籤自動分類、範本與排程傳送、搜尋運算子精準找信。已掛入 `study_guide_app.html` 側邊欄。
- 工具篇總數達 10 篇、演練模組 36 個；Playwright 逐頁點測全數正常。

## @v2.7.0 — 2026-08-16
- **練習環境重新設計**：綠框不再一律掛一份 Docs（Calendar/Meet/Sites 等工具開文件根本練不到），改為依工具性質分六種練習型態：
  `copy` 複製範本／`calendar` 一鍵建立活動／`pair` 兩人一組／`host` 講師開房／`build`·`demo` 自己建一次／`license` 授權限制。各型態有專屬配色與圖示，總覽頁附圖例。
- **檔案型工具改用 `/copy` 強制複製**（13 處）：學員點按鈕會在自己的雲端硬碟產生副本，避免全場共改同一份檔案。
- **Calendar 改用預填活動網址**（3 則）：`calendar.google.com/calendar/render?action=TEMPLATE&…`，情境與待辦已寫進活動說明，學員一點就在自己的日曆開草稿。
- **Classroom／Meet 改為配對與講師開房**：協同教師改兩人互邀、原創性比對改以學生身分加入講師示範課程（教師端看不到的畫面）、分組討論室須自己當主持人才練得到。
- **Sites 加入無痕視窗驗收**：把「預覽正常但外部訪客看到無權限」這個坑變成當場可驗證的動作。
- **Practice Sets 標註授權限制**：需 Education Plus／Teaching & Learning Upgrade，三則演練均附一般帳號的 Google Forms 替代練習。
- **Forms 改為從零自建**（區段跳轉必須自己排過才會懂），並串接到 Sheets 篇做統計。
- 新增統一產線 `scripts/workshop_content.py`（內容單一來源）＋ `scripts/build_workshop_apps.py`（渲染），一次產出全部九篇；
  `build_aligned_tool_apps.py` 與 `reorder_and_align_scenarios.py` 已由其取代。
- Docs 篇納入同一產線，順便修掉總覽區殘留的 Markdown `**` 星號。
- 修正 `all_25_real_workspace_links.json` 兩筆 Sheets 舊網址格式（`/spreadsheet/d/` ➔ `/spreadsheets/d/`）。
- 以 Drive API 實查 25 個範本檔：全部可公開存取且未鎖複製，`/copy` 均可用（**但目前權限為 writer，見 PITFALLS**）。

## @v2.6.0 — 2026-08-16
- 新增 `scripts/build_aligned_tool_apps.py`，以 Docs 工具篇為版型基準，一次重建其餘 8 個工具篇研習 App。
- Slides / Sheets / Classroom / Calendar / Meet / Forms / Sites / Practice Sets 八篇全面升級：每個演練補上【實務教學情境】黃框、真實 Workspace 檔案綠框（含檔名與「本檔具體修改任務」）、步驟勾選清單與一鍵複製，並新增「工具篇總覽與研習目標」首頁模組。
- 演練數由原本 3–5 個零散單元擴充為 26 個完整模組（Classroom / Calendar 各 4、其餘各 3），全部對應 `all_25_real_workspace_links.json` 的真實檔案連結，無死連結。
- 補寫原本缺少的第三演練：Sheets 篩選器檢視與資料驗證、Meet 主持人控制項與分組討論室、Forms 回應驗證與統計、Sites 內嵌動態內容、Practice Sets 作答洞察報告。
- 統一各篇頁首導覽列（回主講義／Docs 工具篇／刷題 App／25 個實作演練）。

## @v2.5.0 — 2026-07-26
- 新增全套 HTML5 互動網頁 App `lab_exercises_app.html`，收錄 15 個 Lab 實作手把手練習單元、進度勾選框與一鍵複製關鍵字功能。
- 升級 `study_guide_app.html` 側邊欄，支援一鍵點擊無縫開啟所有網頁 App 與 Lab 實作模組。

## @v2.0.0 — 2026-07-26
- 完成 Google Level 2 Quiz A 官方 25 題雙語對照題庫 (`GCE_Level_2_Quiz_A_25題完整考題庫.md`) 與 `official_quiz_a_25q.json`。
- 升級 `quiz_app.html` 支援【繁體中文 / English / 中英對照】切換按鈕。
- 整合 3 大官方 Lab Exams (Classroom, Calendar, Slides) 英文原題與繁體中文手把手指南。

## @v1.0.0 — 2026-07-26
- 專案初始化，抓取 Google Teacher Center Level 2 官方 18 個 Lessons 課程內容。
- 建立 Word 排版講義 (.docx)、`EXAM_REGISTRATION_GUIDE.md`、`REFERENCES.md` 與 `study_guide_app.html`。
