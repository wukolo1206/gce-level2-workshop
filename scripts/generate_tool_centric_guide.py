import os

tool_guide_md = """# Google Certified Educator Level 2 - 工具導向考題與實作題手把手對照手冊

> **研習與工具維度分類**：本手冊將 Level 2 的 **25 道選擇題** 與 **3 大 Lab 實作考試**，完全改以 **「Google 工具 (App/Software)」** 為核心分類重新整理。  
> 讓老師在研習學習特定工具（如 Google Docs 或 Google Calendar）時，能一口氣掌握該工具涵蓋的所有選擇題考點與 Lab 實作題目！

---

## 📊 全套工具與考題、實作題快速對照一覽表

| 🛠️ Google 軟體工具 | 📝 涵蓋之選擇題 (Quiz A / Quiz B) | 🎯 選擇題核心考點口訣 | 🛠️ 對應之 Lab 實作題步驟 |
| :--- | :--- | :--- | :--- |
| **1. Google Docs** (文件) | **Q4** (Quiz B Q15)<br>**Q6** (Quiz B Q4)<br>**Q12** (Quiz B Q22)<br>**Q20** (Quiz B Q17) | • Smart Chips (`@People`加`@Date`)指派任務<br>• 段落樣式 (`Headings`) 生成目錄<br>• 尋找與取代 (`Ctrl+H`) 一鍵批次修正<br>• 工具 $\\rightarrow$ 翻譯文件 (`Translate Document`) | **Lab 1 Task 4**：建立班級素材文件<br>**Lab 2 Task 1**：建立會議紀錄附件<br>**Lab 3 Task 3**：註解指派任務 |
| **2. Google Calendar** (日曆) | **Q1** (Quiz B Q3)<br>**Q10** (Quiz B Q7)<br>**Q14** (Quiz B Q21) | • 跨校全年活動排定加 Meet 連結<br>• 親師面談預約時間表 (`Appointment schedule`)<br>• 日曆邀請附加 Docs 會議紀錄 (`Meeting notes`) | **Lab 2 Task 1~5** (完整 Calendar 實作)：<br>• 排定 `Community Fair`<br>• 開啟 Meet 直播 (`Live Stream`)<br>• 輸入地點 `123 Main Street`<br>• 設定 1 小時 Email 提醒<br>• 取消與會者邀請他人與名單權限 |
| **3. Google Classroom** (課堂) | **Q7** (Quiz B Q11)<br>**Q16** (Quiz B Q9)<br>**Q17** (Quiz B Q19) | • 原創性比對報告 (`Originality reports`) 檢查抄襲<br>• 新增跨校夥伴為「協同教師 (`Co-teachers`)」<br>• 建立「測驗作業 (`Quiz Assignment`)」自動匯入成績 | **Lab 1 Task 1~5** (完整 Classroom 實作)：<br>• 建立課程 `Flipped Class`<br>• 從 Sheet 邀請學生與教師<br>• 建立主題 `Term 1` 與 `Term 2`<br>• 建立作業 `Unit 1` 與素材<br>• 發布含 Meet 連結與守則之公告 |
| **4. Google Slides** (簡報) | **Q18** (Quiz B Q8)<br>**Q21** (Quiz B Q16)<br>**Q25** (Quiz B Q13) | • 插入選單或右鍵選單建立超連結<br>• 內嵌 YouTube 影片 (`Embed YouTube`) 提升互動<br>• 投影片互相建立超連結 (`Hyperlink Slides`) 製作記憶卡 | **Lab 3 Task 1~5** (完整 Slides 實作)：<br>• 建立 `Welcome to Our Team` 簡報<br>• 插入圖片 `handclap.png`<br>• 主題建構工具設 `Image Placeholder`<br>• 內嵌影片 `Meet Our New Teachers.mp4`<br>• 批註 `+Email` 並勾選 `Assign to...` |
| **5. Google Sites** (協作平台) | **Q2** (Quiz B Q24)<br>**Q11** (Quiz B Q5)<br>**Q23** (Quiz B Q14) | • PBL 專題展示：提供每生專屬子頁面 (`Subpage`)<br>• 權限調整：進入「發布 (`Publish`)」設定<br>• 外部大學審閱：網站設 `Public` / 文件設 `Publish to web` | **PBL 專題與學習歷程展示**：<br>• 新增頁面導覽<br>• 內嵌 Docs / Slides / YouTube 多媒體<br>• 設定公開發布權限 |
| **6. Google Sheets** (試算表) | **Q9** (Quiz B Q10)<br>**Q15** (Quiz B Q12) | • 根據分數自動變更格子顏色：條件式格式化<br>• 統計表單投票：直行統計 (`Column stats`) 與樞紐分析表 | **資料清理與數據分析**：<br>• 匯入學生成績與表單回應<br>• 設定條件式格式紅底白字<br>• 生成直行統計圖表與樞紐分析 |
| **7. Google Meet** (視訊會議) | **Q5** (Quiz B Q2)<br>**Q24** (Quiz B Q6) | • 網路連線不穩定：透過電話撥號加入 (`Join by phone`)<br>• 檔案內協作：Docs/Slides 內直接發起或加入 Meet | **Lab 2 Task 2**：在 Calendar 開啟 Meet 直播<br>**Lab 1 Task 5**：將 Meet 網址貼至 Classroom 公告 |
| **8. Practice Sets** (練習組) | **Q8** (Quiz B Q18)<br>**Q19** (Quiz B Q20) | • 設定多達 10 個提示資源：額外協助 (`Extra help`)<br>• 團隊共享：開啟連結共用 (`Turn on link sharing`) | **差異化學習與腳手架**：<br>• 為練習題加入 YouTube 影片提示<br>• 複製連結共用給備課團隊 |
| **9. Workspace Marketplace** | **Q3** (Quiz B Q1) | • 在 Docs 給予非同步口頭語音回饋：搜尋 Add-on (Mote) | **擴充功能安裝與應用**：<br>• 點選「擴充功能 $\\rightarrow$ 外掛程式」搜尋安裝 |
| **10. Google Forms** (表單) | **Q13** (Quiz B Q23) | • 翻轉課堂：表單加入教學影片並設定依回應跳轉區段 | **單元形成性評量與翻轉教學**：<br>• 設為測驗 (Quiz)<br>• 設定區段跳轉實施差異化 |

---

## 🛠️ 各工具手把手細節與實作演練步驟

### 📄 1. Google Docs (文件)
- **選擇題考點**：
  - 📝 **Q4 / Quiz B Q15 (Smart Chips)**：在 Docs 輸入 `@` 選取 `@People` 指派任務，選取 `@Date` 設定截止日。
  - 📝 **Q6 / Quiz B Q4 (Paragraph Styles)**：套用「標題 1 (Heading 1)」等段落樣式，點選「插入 $\\rightarrow$ 目錄」自動生成目錄。
  - 📝 **Q12 / Quiz B Q22 (Find & Replace)**：按 `Ctrl+H` 搜尋錯誤作者姓名並點選「全部替換」。
  - 📝 **Q20 / Quiz B Q17 (Translate Document)**：點選「工具 $\rightarrow$ 翻譯文件」產生多語言班級通訊。
- **對應 Lab 實作題步驟**：
  - 🛠️ **Lab 1 Task 4**：在 Classroom 建立 `Unit 1 Readings` 素材並附加 Docs 文件。
  - 🛠️ **Lab 2 Task 1**：在 Calendar 活動點選「新增會議紀錄 (Add meeting notes)」自動生成並附加 Docs。

---

### 📅 2. Google Calendar (日曆)
- **選擇題考點**：
  - 📝 **Q1 / Quiz B Q3 (Meet Integration)**：全年跨校活動在 Calendar 排定，並附加 Google Meet 視訊連結。
  - 📝 **Q10 / Quiz B Q7 (Appointment Schedule)**：親師面談點選「建立 $\rightarrow$ 預約時間表」，生成公開 URL 讓家長點選預約。
  - 📝 **Q14 / Quiz B Q21 (Meeting Notes)**：日曆邀請點選「新增會議紀錄 (Meeting notes)」，自動分發 Docs 給所有與會者。
- **對應 Lab 實作題步驟**：
  - 🛠️ **Lab 2 Task 1**：建立 `Community Fair` 活動，時間設為下週五 `3:00 PM - 4:00 PM`。
  - 🛠️ **Lab 2 Task 2**：點選 Google Meet 視訊設定選單，點選「新增串流直播 (Add live stream)」。
  - 🛠️ **Lab 2 Task 3**：新增地點 `123 Main Street`。
  - 🛠️ **Lab 2 Task 4**：新增通知選取 `Email`，時間設定為 `1 小時前 (1 hour before)`。
  - 🛠️ **Lab 2 Task 5**：新增與會者，並在與會者權限中**取消勾選「邀請他人 (Invite others)」與「檢視與會者名單 (See guest list)」**。

---

### 🏫 3. Google Classroom (課堂)
- **選擇題考點**：
  - 📝 **Q7 / Quiz B Q11 (Originality Reports)**：作業勾選「原創性比對報告」，允許學生提交前自主檢查抄襲。
  - 📝 **Q16 / Quiz B Q9 (Co-teachers)**：跨校交流點選「成員 $\rightarrow$ 新增教師」，將夥伴新增為協同教師 (`Co-teachers`)。
  - 📝 **Q17 / Quiz B Q19 (Quiz Assignment)**：建立「測驗作業 (Quiz Assignment)」，確保開啟右側「成績匯入 (Grade importing)」。
- **對應 Lab 實作題步驟**：
  - 🛠️ **Lab 1 Task 1**：在 Classroom 點選 `+` 建立新課程，名稱精確輸入 `Flipped Class`。
  - 🛠️ **Lab 1 Task 2**：開啟 `5th Grade List` Sheet，將 Email 複製並邀請為學生與協同教師。
  - 🛠️ **Lab 1 Task 3**：進入「課堂作業」點選「建立 $\rightarrow$ 主題」，分別建立 `Term 1` 與 `Term 2` 主題。
  - 🛠️ **Lab 1 Task 4**：在 `Term 1` 主題下建立作業 `Unit 1`（總分 10 分）與素材 `Unit 1 Readings`。
  - 🛠️ **Lab 1 Task 5**：在「訊息串」發布公告，內含 Google Meet 連結與 4 條班級守則。

---

### 🎨 4. Google Slides (簡報)
- **選擇題考點**：
  - 📝 **Q18 / Quiz B Q8 (Link Media)**：點選「插入 $\rightarrow$ 連結」或按右鍵選取「連結」加入外部資源。
  - 📝 **Q21 / Quiz B Q16 (Embed YouTube)**：點選「插入 $\rightarrow$ 影片」直接在投影片內嵌 YouTube 教學影片。
  - 📝 **Q25 / Quiz B Q13 (Hyperlink Slides)**：物件按右鍵選「連結 $\rightarrow$ 簡報中的投影片」，互相建立超連結製作單字記憶卡。
- **對應 Lab 實作題步驟**：
  - 🛠️ **Lab 3 Task 1**：建立新簡報命名為 `Welcome to Our Team`，首頁插入圖片 `handclap.png`。
  - 🛠️ **Lab 3 Task 2**：建立 3 位教師投影片，並在「主題建構工具 (Theme Builder)」插入「圖片預留位置 (`Image Placeholder`)」。
  - 🛠️ **Lab 3 Task 3**：選取簡報元件新增註解，輸入 `+成員Email` 並**勾選「指派給... (Assign to...)」**小方塊。
  - 🛠️ **Lab 3 Task 4**：點選「插入 $\rightarrow$ 影片」內嵌影片檔案 `Meet Our Amazing New Teachers.mp4`。
  - 🛠️ **Lab 3 Task 5**：點選「共用」，新增教育主管 Email 並將權限設定為「註解者 (Commenter)」。

---

### 🌐 5. Google Sites (協作平台)
- **選擇題考點**：
  - 📝 **Q2 / Quiz B Q24 (Student Portfolios)**：PBL 專題成果展示建立 Google Sites，並給予每生一個專屬子頁面 (`Subpage`)。
  - 📝 **Q11 / Quiz B Q5 (Publish Settings)**：網站要開放給特定師生檢視，必須點選右上角「發布 (Publish)」進行權限設定。
  - 📝 **Q23 / Quiz B Q14 (Public Access)**：作品集開放給外部大學審閱，發布的網站設 `Public`，內嵌文件設 `Publish to the web`。

---

### 📊 6. Google Sheets (試算表)
- **選擇題考點**：
  - 📝 **Q9 / Quiz B Q10 (Conditional Formatting)**：依學生分數表現自動改變格子顏色，使用「條件式格式設定 (Conditional Formatting)」。
  - 📝 **Q15 / Quiz B Q12 (Column Stats & Pivot Table)**：統計表單投票得票數，使用「直行統計 (Column stats)」與「樞紐分析表 (Pivot table)」。

---

### 📹 7. Google Meet (視訊會議)
- **選擇題考點**：
  - 📝 **Q5 / Quiz B Q2 (Join by Phone)**：網路連線斷斷續續不穩定時，使用「透過電話撥號加入 (Join by phone)」。
  - 📝 **Q24 / Quiz B Q6 (In-Doc Integration)**：在 Google Docs/Slides 頂部工具列直接發起或快速加入 Meet 會議。
- **對應 Lab 實作題步驟**：
  - 🛠️ **Lab 2 Task 2**：在 Calendar 活動設定中點選 Meet，開啟「串流直播 (Live stream)」。
  - 🛠️ **Lab 1 Task 5**：將 Meet 會議連結貼至 Classroom 訊息串公告中。
"""

with open(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\docs\GCE_Level_2_工具導向考題與實作題對照手冊.md', 'w', encoding='utf-8') as f:
    f.write(tool_guide_md)

print("Successfully generated GCE_Level_2_工具導向考題與實作題對照手冊.md!")
