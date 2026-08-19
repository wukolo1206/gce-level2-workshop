# Google Certified Educator Level 2 全套研習講義與備考工具包

本工具包收錄對照 Google 官方 Teacher Center 最新 **Level 2 (Google 認證教育者第 2 級)** 課程所製作之繁體中文全方位研習講義、報名流程教學、25 題雙語對照真題庫、15 個實作 Lab 演練手冊與三款 HTML5 網頁應用程式。

---

## 📂 整理後之資料夾目錄結構與檔案說明

### 🌐 1. 主網頁入口 (HTML Web Applications)
- 📖 **[study_guide_app.html](file:///d:/備課ai/研習講義/Google認證_Level2_研習講義與備考工具包/study_guide_app.html)** (推薦首選)：
  - **研習講義與備考總系統**：包含 6 大單元圖文對照、官方報名流程、考前 15 分鐘速記卡與側邊欄無縫整合。
- 📝 **[quiz_app.html](file:///d:/備課ai/研習講義/Google認證_Level2_研習講義與備考工具包/quiz_app.html)**：
  - **25 題雙語線上刷題 App**：收錄 Quiz A 官方 25 題實務真題，支援【繁體中文 / English / 中英對照】切換。
- 🛠️ **[lab_exercises_app.html](file:///d:/備課ai/研習講義/Google認證_Level2_研習講義與備考工具包/lab_exercises_app.html)**：
  - **15 個 Lab 實務操作演練網頁 App**：提供步驟進度 Checkboxes 與關鍵字一鍵複製按鈕。

---

### 📘 2. 講義與說明文件庫 (`docs/`)
- 📋 **[EXAM_REGISTRATION_GUIDE.md](file:///d:/備課ai/研習講義/Google認證_Level2_研習講義與備考工具包/docs/EXAM_REGISTRATION_GUIDE.md)**：官方報名 5 大步驟與 6 大考場實景圖解。
- 📘 **[GCE_Level_2_Quiz_A_25題完整考題庫.md](file:///d:/備課ai/研習講義/Google認證_Level2_研習講義與備考工具包/docs/GCE_Level_2_Quiz_A_25題完整考題庫.md)**：25 題官方真題中英雙語完整考題庫。
- 🛠️ **[GCE_Level_2_Lab_Exams_15個實務操作練習題庫與學習手冊.md](file:///d:/備課ai/研習講義/Google認證_Level2_研習講義與備考工具包/docs/GCE_Level_2_Lab_Exams_15個實務操作練習題庫與學習手冊.md)**：15 個 Lab 實作手把手練習手冊。
- 🛠️ **Lab 1/2/3 獨立指南**：`GCE_Level_2_Lab_1_Classroom_實作題完整指南.md`、`GCE_Level_2_Lab_2_Calendar_實作題完整指南.md`、`GCE_Level_2_Lab_3_Slides_實作題完整指南.md`。
- ⚡ **[Google_Level_2_精華速記卡.md](file:///d:/備課ai/研習講義/Google認證_Level2_研習講義與備考工具包/docs/Google_Level_2_精華速記卡.md)**：考前 15 分鐘極速衝刺速查表。
- 🔗 **[REFERENCES.md](file:///d:/備課ai/研習講義/Google認證_Level2_研習講義與備考工具包/docs/REFERENCES.md)**：18 個 官方 Lessons 網址與追蹤清單。

---

### 📦 3. 數據資料庫 (`data/`)
- `official_quiz_a_25q.json`：25 題雙語考題數據庫。
- `official_course_dump.json`：18 個 Lessons 課程網頁抓取數據庫。

---

### 🛠️ 4. 構建腳本 (`scripts/`)
- `build_quiz_app.py`、`build_lab_exercises_app.py`、`fetch_course_details.py`、`make_word_doc.py`、`copy_images.py`。

---

### 🖼️ 5. 圖片庫 (`images/`)
- 收錄考場選單、報名完成、資格驗證、言語切換與各項功能介面實景圖片。

---

### 📄 6. Word 講義與專案維護檔案
- `Google_Certified_Educator_Level_2_講義.docx` (可供列印之 Word 檔)
- `AGENTS.md` / `CLAUDE.md` / `CHANGELOG.md` / `PITFALLS.md` / `DECISIONS.md` / `handoff.md`
