# Google Workspace 教育應用研習講義

以**工具**為主軸的 Google Workspace 教師研習講義，共十個工具、**40 個實務演練**。
每一則演練都包含真實教學情境、可實際動手的練習環境，以及可逐項打勾的操作步驟。

👉 **線上閱讀**：<https://wukolo1206.github.io/gce-level2-workshop/>

## 特色

**每則演練都給得出真正能練的環境**，而不是只給一份說明文件：

| 練習方式 | 適用 | 做法 |
|---|---|---|
| 📄 複製範本 | Docs／Sheets／Slides | 點按鈕建立你自己的副本，改壞了也沒關係 |
| ⚡ 一鍵建立 | Calendar | 直接在你自己的日曆開一個已填好內容的活動草稿 |
| 👥 兩人一組 | 協同教師、帳戶代理 | 需要另一個人才練得到，附角色分工 |
| 🎙️ 講師開房 | Meet、學生視角體驗 | 講師開好會議室或課程，學員進去實測 |
| 🔨 自己建一次 | Forms、Sites | 沒有範本，從空白做一次（這類功能自己排過才會懂） |
| ⚠️ 需付費授權 | Practice Sets | 標註授權門檻，並附一般帳號的替代練習 |

**每篇都附中英術語對照表**，因為 Google 介面可切換語言、官方文件也多用英文。

## 十篇工具講義

| 工具 | 演練數 | 內容 |
|---|---|---|
| [Google Docs](docs_workshop_app.html) | 7 | 智慧晶片、段落樣式、翻譯、探索學習單 |
| [Google Classroom](classroom_workshop_app.html) | 5 | 協同教師、主題、成績匯入、公告 |
| [Google Calendar](calendar_workshop_app.html) | 5 | 預約表、直播、權限、會議記錄、系列活動 |
| [Google Slides](slides_workshop_app.html) | 4 | 超連結、母版、內嵌影片、分享權限 |
| [Gmail](gmail_workshop_app.html) | 4 | 帳戶代理、篩選器、範本排程、搜尋運算子 |
| [Google Sheets](sheets_workshop_app.html) | 3 | 條件式格式、樞紐分析、篩選器檢視畫面 |
| [Google Meet](meet_workshop_app.html) | 3 | 電話備援、檔案內視訊、分組討論室 |
| [Google Forms](forms_workshop_app.html) | 3 | 區段跳轉、測驗評分、回應驗證 |
| [Google Sites](sites_workshop_app.html) | 3 | 子頁面、發布權限、內嵌動態內容 |
| [Practice Sets](practicesets_workshop_app.html) | 3 | 額外協助、題組共享、課程深入分析 |

另附[**課程結構對照**](course_structure_map.html)：官方繁體中文版（11 個實務單元）與英文版
（6 Units / 18 Lessons）的目錄完全不同，這張表把兩者與十篇工具講義對起來，
並保留「一個教學情境要串哪幾個工具」的綜合應用視角。

## 帳號授權提醒

部分功能需要付費授權，講義中都已標註並附替代練習：

| 功能 | 個人 Gmail | Education Fundamentals | Education Plus / T&L |
|---|---|---|---|
| Meet 串流直播 | ❌ | ❌ | ✅ |
| Meet 分組討論室（當主持人） | ❌ | ✅ | ✅ |
| Classroom 原創性比對 | ❌ | ✅ | ✅ |
| Practice Sets | ❌ | ❌ | ✅ |

## 如何修改內容

所有講義由腳本產生，**不要直接改 HTML**：

```bash
# 1. 改內容（40 個演練的情境與步驟）
scripts/workshop_content.py

# 2. 改中英術語表
scripts/workshop_glossary.py

# 3. 重新產生
python scripts/build_workshop_apps.py        # 十篇工具講義
python scripts/build_course_structure_map.py # 課程結構對照
python scripts/build_public_index.py         # 首頁與公開版打包
```

## 內容正確性

講義中的介面名稱與選單路徑經過兩輪 AI 交叉審查與官方說明頁查證，
修正了 12 處名稱錯誤與多處步驟前置條件（例如 Gmail 帳戶代理接受後最多需 24 小時才生效、
Classroom 排定發布的公告不會出現在訊息串因此無法置頂）。

Google 的介面文案改版頻繁，若你發現任何名稱與現況不符，歡迎開 Issue 指正。

## 授權

講義內容為原創教學設計，歡迎教育工作者自由取用與改編。
Google、Google Workspace、Google Classroom 等為 Google LLC 的商標，本專案與 Google 無關。
