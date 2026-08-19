---
project: Google認證_Level2_研習講義與備考工具包
category: 學科工具集 / 教學工具
status: 穩定
version: v3.1.3
url: "https://wukolo1206.github.io/gce-level2-workshop/"
next_action: 待使用者裁決是否改寫公開 repo git 歷史，清除仍留在舊 commit 的未打碼考場截圖（cc82fba 起）；另待用真實帳號走完 實測檢核表.md 的 94 項介面核對、研習現場試講。
updated: 2026-08-18
---

# CLAUDE.md — Google認證 Level 2 研習講義與備考工具包

本專案收錄 Google Certified Educator Level 2 (Google 認證教育者第 2 級) 完整官方 6 大單元研習講義、報名教學、考前速記卡、25 題雙語線上刷題系統與 15 個實戰操作實驗 (Lab Exams) 網頁 App。

## 技術框架
- **前端 Web App**：HTML5, Vanilla CSS, Javascript (ES6+, Single Page Applications)
- **數據構建與轉換**：Python 3 (json, docx, pillow)
- **視覺與設計**：Google Material Design / Modern CSS Tokens, High contrast HSL Palette

## 不能動的地方
- 官方 25 題試題 JSON (`official_quiz_a_25q.json`) 的題幹與標準解答。
- 6 張官方考場與認證控制台實景圖片 (位於 `images/` 目錄)。

## 部署與驗證

### 兩個 GitHub repo
| 用途 | Repo | 內容 |
| --- | --- | --- |
| 公開（學員用） | `wukolo1206/gce-level2-workshop` | 十篇工具講義＋課程結構對照＋首頁＋產生器 |
| 私人（完整備份） | `wukolo1206/gce-level2-workshop-private` | 本資料夾全部內容（含題庫、Lab 指南、講師版、審查紀錄） |

線上網址：<https://wukolo1206.github.io/gce-level2-workshop/>

**公開版絕不可包含**：官方題庫（`data/`、`docs/*Quiz*`）、Lab 實作題指南、考場實景截圖、
講師版對照表、`study_guide_app.html`（該頁夾帶考場截圖與報名教學）。
由 `scripts/build_public_index.py` 控制打包白名單，勿手動複製檔案進公開 repo。

### 更新流程
```bash
# 1. 改內容（唯一來源）
scripts/workshop_content.py      # 40 個演練
scripts/workshop_glossary.py     # 中英術語表

# 2. 重建
python scripts/build_workshop_apps.py         # 十篇工具講義
python scripts/build_course_structure_map.py  # 課程結構對照
python scripts/build_public_index.py          # 打包公開版到 C:\repos\gce-level2-workshop

# 3. 推送
git add -A && git commit -m "..." && git push                    # 本資料夾 → 私人 repo
cd C:\repos\gce-level2-workshop && git add -A && git commit -m "..." && git push   # → 公開 repo（Pages 自動更新）
```

⚠️ 公開版輸出目錄刻意放在 **`C:\repos\`（Drive 同步範圍外）**：放在 `D:\備課ai\` 底下會被 Google Drive
鎖檔導致建置失敗，且等於整份重複上傳雲端。

### 驗證方式
- 本機：雙擊 `study_guide_app.html` 確認十篇工具講義與各分頁切換正常。
- 線上：確認 <https://wukolo1206.github.io/gce-level2-workshop/> 回應 200 且圖片正常。
