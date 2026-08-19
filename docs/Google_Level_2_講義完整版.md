# Google Certified Educator Level 2 認證考試研習講義（官方圖文對照版）

> **官方課程來源**：[Google for Education - Intermediate use of Google Workspace for Education Fundamentals](https://edu.exceedlms.com/student/path/1717663?locale=zh_tw)
> **編寫說明**：本講義完全對照 Google 官方 Teacher Center 最新 Level 2 (中級應用) 課程之 6 大核心單元與 Knowledge Check 實務隨堂評量，精準剖析各單元的教學設計重點、實作工具、函數語法與情境考點，並嵌入高質感功能操作示意圖。

---

## 📌 課程架構與認證準備策略

Google Certified Educator Level 2 旨在認證能夠利用 Google Workspace 工具進行**自動化工作流程、親師溝通、數位教材組織、互動學習環境、差異化教學與數據分析**的教育專家。

### 💡 官方 6 大核心單元對照表
| 官方單元名稱 (Unit Name) | 核心工具與重點知能 | 實作與情境考點 |
| :--- | :--- | :--- |
| **Unit 1: 自動化課堂與行政任務** | Gmail 篩選器/標籤, **自動進階 (Auto-advance)**, Smart Canvas, Add-ons | 郵件自動分類、刪除/封存後自動顯示下一封、`@` 智慧標籤協作 |
| **Unit 2: 與家長及監護人高效溝通** | Google Forms, Calendar 預約時間表, Google Meet | 監護人資料收集與驗證、親師座談預約網址生成 |
| **Unit 3: 系統化組織班級與教學素材** | Google Docs 書籤/目錄, Google Drive, Google Sites | 數位課程大綱 (Syllabus)、學生數位學習歷程 (Portfolio) |
| **Unit 4: 打造互動式自主學習環境** | Google Slides 互動導覽, Google Meet, YouTube | 非線性選單 (Choice Boards)、觀眾問答 (Q&A)、跨國連線 |
| **Unit 5: 實施學生個人化與差異化學習** | Classroom 分組派發, Blogger, 學習成果視覺化 | 個別化作業派發、適應性測驗跳轉、學生線上作品集 |
| **Unit 6: 分析與解讀學生學習數據** | Google Sheets (QUERY/IMPORTRANGE), Pivot Table | 跨表資料拉取、SQL 篩選、條件式格式化亮紅燈警示 |

---

## 📖 第一章：自動化課堂與行政任務 (Unit 1: Automate classroom tasks)

在繁重的教學與行政工作中，透過數位工具自動化流程，能為教師省下寶貴時間。

### 1.1 Boost your efficiency in Gmail (提升 Gmail 郵件處理效率)

#### 1. 高階進階功能：自動進階 (Auto-advance) **【官方必考隨堂測驗題】**
*   **功能與描述**：一般情況下，刪除或封存郵件時系統會返回收件匣。啟用 **「自動進階 (Auto-advance)」** 後，系統會在刪除/封存目前郵件後，**自動直接顯示下一封未讀郵件**，無須頻繁返回收件匣，大幅節省批次處理未讀郵件的時間。
*   **設定路徑**：Gmail 設定 (齒輪) $\rightarrow$ 觀看所有設定 $\rightarrow$ 「進階」分頁 $\rightarrow$ 啟用「自動進階 (Auto-advance)」。

![Gmail Auto-advance 功能介面示意圖](images/gmail_auto_advance.jpg)

#### 2. 郵件篩選器 (Filters) 與標籤 (Labels)
*   **應用**：自動將班級家長郵件歸類至「家長來信」標籤，或自動標示星號與轉寄。
*   **設定步驟**：搜尋欄點選「顯示搜尋選項」 $\rightarrow$ 輸入篩選條件（如 `from:parent@school.edu`） $\rightarrow$ 點選「建立篩選器」 $\rightarrow$ 勾選「套用標籤」或「通通跳過收件匣」。

#### 3. 範本郵件 (Templates / 罐頭回應)
*   **應用**：針對常見親師詢問，預先撰寫回覆範本，一鍵帶入。

---

### 1.2 Explore add-ons in Google Workspace for Education (擴充功能與 Add-ons)
*   ** Workspace Add-ons (外掛擴充)**：
    *   在 Google Docs、Forms、Sheets 右側側邊欄點選 `+` 號安裝，如 Autocrat（自動化產出 PDF 證書）、FormMule（自動發送通知信）。

### 1.3 Level up collaboration with smart canvas (智慧畫布與智慧標籤)
*   **智慧標籤 (Smart Chips)**：
    *   在 Docs 或 Sheets 中輸入 `@` 符號，可快速插入：
        *   **人員標籤 (`@成員姓名`)**：直接指派任務並給予檔案權限。
        *   **檔案標籤 (`@檔名`)**：內嵌關聯 Google Drive 文件預閱卡片。
        *   **日期標籤與會議紀錄範本 (`@Date` / `@Meeting notes`)**：一鍵帶入 Calendar 會議細節與待辦事項清單。

![Google Docs Smart Canvas 智慧標籤示意圖](images/smart_canvas_chips.jpg)

---

## 👨‍👩‍👧 第二章：與家長及監護人高效溝通 (Unit 2: Communicate with parents and guardians)

建立順暢且專業的親師溝通管道，同時降低教師行政負擔。

### 2.1 Organize guardian information with Google Forms (表單收集與資料驗證)
*   **資料驗證 (Data Validation)**：
    *   在收集家長電話或 Email 時，設定強制的輸入格式限制。
    *   **操作步驟**：簡答題 $\rightarrow$ 右下角三點 $\rightarrow$ 「驗證回應」 $\rightarrow$ 文字 $\rightarrow$ 電子郵件位址；或設定數字與長度限制。

### 2.2 Create a communication system with Google tools (建立雙向溝通機制)
*   **Classroom 監護人摘要 (Guardian Summaries)**：邀請家長接收每週或每日的未繳作業與課堂公告摘要。
*   **Google Group 協作收件匣 (Collaborative Inbox)**：用作親師諮詢信箱，團隊成員可相互指派信件。

### 2.3 Manage meetings with Google Workspace for Education (親師座談與會談預約)
*   **Google Calendar 預約時間表 (Appointment Schedules)**：
    *   **應用**：自訂親師座談會或輔導時段，開放家長線上預約。
    *   **操作步驟**：行事曆點選「建立」 $\rightarrow$ 「預約時間表」 $\rightarrow$ 設定可預約時段與每場次時間（如 15 分鐘） $\rightarrow$ 系統自動產生外部分享連結，家長預約後自動連動 Meet 連結與通知。

![Google Calendar 預約時間表介面示意圖](images/calendar_appointments.jpg)

---

## 📂 第三章：系統化組織班級與教學素材 (Unit 3: Organize your class materials)

### 3.1 Create a digital syllabus in Google Docs (數位課程大綱)
*   **書籤 (Bookmark) 與內部導覽連結**：
    *   **步驟**：選取目標文字 $\rightarrow$ 插入 $\rightarrow$ **書籤 (Bookmark)** $\rightarrow$ 在目錄文字處設定超連結連至該書籤。
*   **自動生成目錄 (Table of Contents)**：套用「標題 1」、「標題 2」樣式後，插入 $\rightarrow$ 目錄。

### 3.2 Create digital portfolios with Google Drive and Sites (數位學習歷程檔案)
*   **Google Sites 專題網頁製作**：學生整合個人作業、圖片、YouTube 影片，並利用「在導覽列中隱藏」設定審查用頁面。

---

## 🎮 第四章：打造互動式自主學習環境 (Unit 4: Create an interactive learning environment)

### 4.1 Deliver interactive presentations with Google Slides (非線性互動簡報)
*   **選擇板 / 冒險選單 (Choice Boards)**：
    *   利用簡報按鈕，設定超連結指向「這份簡報中的投影片」。
    *   將解答頁設定為「**隱藏投影片 (Hide slide)**」，避免直接按下一頁洩漏解答。
*   **觀眾問答 (Audience Q&A)**：開啟提問網址進行匿名或具名提問與按讚投票。

### 4.2 Use Google Meet to connect to the world (遠距共學)
*   **進階 Meet 功能**：小組討論分組分流 (Breakout Rooms)、即時問答與投票 (Q&A and Polls)。

---

## 🎯 第五章：實施學生個人化與差異化學習 (Unit 5: Personalize student learning)

### 5.1 Share personalization options using Google Workspace (差異化教學策略)
*   **Classroom 個別指派**：取消勾選「所有學生」，針對補救或資優分組派發。
*   **Forms 適應性路徑 (Branching Logic)**：單選題/下拉題設定「根據回應跳轉至指定區段」。

### 5.2 Publish work online using Google tools (線上作品發布與 Blogger)
*   **Blogger 專題網誌**：透過標籤 (Tags) 管理專題類別與學生作品發表。

---

## 📈 第六章：分析與解讀學生學習數據 (Unit 6: Analyze and interpret student data)

### 6.1 Deliver formative assessments with Classroom and Forms (形成性評量)
*   設定答對與答錯時各自顯示的影音或文字回饋連結。

### 6.2 Analyze data in Google Sheets (高階數據分析函數)
*   **`QUERY` SQL 查詢**：
    ```excel
    =QUERY(A1:E100, "SELECT A, B WHERE C < 60 AND E = '401' ORDER BY C ASC", 1)
    ```
*   **`IMPORTRANGE` 跨表連線**：
    ```excel
    =IMPORTRANGE("目標試算表URL", "工作表1!A1:D50")
    ```
    *   *首次連線必須點選「允許存取 (Allow Access)」*。

### 6.3 Visualize student results (數據視覺化)
*   **樞紐分析表 (Pivot Table)**：交錯分析各班平均表現。
*   **條件式格式化**：自動亮紅燈標示學習預警名單。

![Google Sheets QUERY 函數與數據分析介面示意圖](images/sheets_data_query.jpg)

---
*本講義內容完全符合 Google 官方 Teacher Center 課程與 Knowledge Check 標準*
