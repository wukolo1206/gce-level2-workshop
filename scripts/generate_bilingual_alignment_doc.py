import os

doc_md = """# Google Certified Educator Level 2 中英文架構、專業術語與意同對照指南

> **研習與備考關鍵**：正式 GCE Level 2 認證考試包含英文與中英雙語題目，而 Google 官方 Teacher Center 提供了 11 個單元的繁體中文研習課程。  
> 為避免學員因「中文習慣用語」與「英文考題原詞」對不上而失分，本指南為講師與學員提供完整的 **【英文考綱術語 $\\Leftrightarrow$ 繁體中文官方術語 $\\Leftrightarrow$ 11 個實務單元意同對照】**。

---

## 📊 1. 核心考點專業術語中英文意同對照表

| 英文認證考綱術語 (English Exam Term) | 官方繁體中文術語 (zh-TW Official Term) | 對應 6 大考綱 | 對應 11 個實務單元 | 🎯 考試應試與解題關鍵 (Exam Key Focus) |
| :--- | :--- | :---: | :---: | :--- |
| **Appointment schedule** | 預約時間表 | Unit 2 | 第 4 單元 | 親師面談自動呈現空閒時段與公開 URL 連結 |
| **Grant access to your account** | 授予您帳戶的存取權 (帳戶代理) | Unit 1 | 第 3 單元 | 團隊成員免告知密碼代表主管收發 Email |
| **Paragraph styles (Headings)** | 段落樣式 (標題 1、標題 2) | Unit 3 | 第 6 單元 | Google Docs 自動生成 Table of Contents (目錄) |
| **Originality reports** | 原創性比對報告 | Unit 3 | 第 9 單元 | Classroom 學生提交作業前自主比對抄襲 |
| **Conditional Formatting** | 條件式格式設定 | Unit 6 | 第 5 單元 | Sheets 根據分數表現自動變更儲存格背景顏色 |
| **Quiz Assignment & Grade importing** | 測驗作業 與 成績匯入 | Unit 3 | 第 11 單元 | Forms 測驗分數自動同步傳送至成績冊 (Grades tab) |
| **Smart Chips (@People / @Date)** | 智慧晶片 (@人員 / @日期) | Unit 1 | 第 1 單元 | Docs 議程指派任務給個人並設定截止日期 |
| **Join by phone** | 透過電話撥號加入 | Unit 4 | 第 8 單元 | Meet 視訊在網路連線不穩定時之語音備援 |
| **Workspace Marketplace Add-ons** | Workspace Marketplace 外掛程式 | Unit 5 | 第 3 單元 | 在 Google Docs 提供非同步語音回饋 (Mote) |
| **Hyperlink Slides to each other** | 投影片互相建立超連結 | Unit 4 | 第 7 單元 | Slides 製作單字記憶卡與互動選擇板 (Choice Boards) |
| **Co-teachers** | 協同教師 | Unit 2 | 第 3 單元 | 跨校/跨班專案多位老師共同管理 Classroom |
| **Translate Document** | 翻譯文件 | Unit 2 | 第 9 單元 | 將班級每週通訊一鍵翻譯為多國語言 (越南語等) |
| **Embed a YouTube video** | 內嵌 YouTube 影片 | Unit 4 | 第 7 單元 | Slides 簡報直接插入影片提升互動性 |
| **Column stats & Pivot table** | 直行統計 與 樞紐分析表 | Unit 6 | 第 5 單元 | Sheets 快速統計表單投票回應與資料分析 |
| **Turn on link sharing** | 開啟連結共用 | Unit 5 | 第 1 單元 | 教師團隊共享 Practice sets 練習組資源 |
| **Extra help** | 額外協助 | Unit 5 | 第 1 單元 | Practice sets 中設定多達 10 個提示/影片資源 |
| **Public & Publish to the web** | 公開 與 發布至網路 | Unit 3 | 第 10 單元 | 數位作品集 (Sites) 開放給大學評審審閱 |

---

## 🌐 2. 中英文架構對照（6 大考綱 vs 11 個實務單元）

- **考綱領域 Unit 1 (自動化行政)** $\\Leftrightarrow$ **中文第 1, 3 單元**（智慧晶片、代理授權、取代）
- **考綱領域 Unit 2 (親師溝通與跨校)** $\\Leftrightarrow$ **中文第 4, 8 單元**（預約時間表、跨校 Meet、翻譯）
- **考綱領域 Unit 3 (班級素材管理)** $\\Leftrightarrow$ **中文第 6, 9, 10 單元**（Sites 作品集、段落樣式目錄、原創性比對）
- **考綱領域 Unit 4 (互動學習環境)** $\\Leftrightarrow$ **中文第 7, 8 單元**（Slides 超連結、記憶卡、Meet 電話撥號）
- **考綱領域 Unit 5 (差異化與個人化)** $\\Leftrightarrow$ **中文第 1, 2, 3 單元**（Practice sets 額外協助、Marketplace 語音回饋）
- **考綱領域 Unit 6 (數據解讀與分析)** $\\Leftrightarrow$ **中文第 5 單元**（條件式格式、直行統計、樞紐分析）
"""

with open(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\docs\GCE_Level_2_中英文對照與專業術語意同比對指南.md', 'w', encoding='utf-8') as f:
    f.write(doc_md)

print("Successfully generated GCE_Level_2_中英文對照與專業術語意同比對指南.md!")
