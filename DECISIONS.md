# DECISIONS.md — 架構決策記錄

## 採用全套單頁 HTML5 Web App 作為研習與備考交付載體

**選擇：**
放棄單純提供 PDF/Markdown 靜態文件，全面採用 HTML5 單頁應用程式 (SPAs) (`study_guide_app.html`, `quiz_app.html`, `lab_exercises_app.html`)。

**原因：**
1. **互動體驗提升**：提供【繁體中文 / English / 中英對照】語系即時切換、刷題即時計分與詳細考點解析。
2. **零安裝成本**：老師與學員無須安裝任何軟體或 Python 環境，雙擊即可在 Chrome/Edge 開啟使用。
3. **實戰方便性**：在 `lab_exercises_app.html` 中提供步驟 Checkbox 與一鍵複製關鍵字功能，便於一邊對照網頁一邊操作 Google 軟體。

**棄選方案：**
- 僅產出 Word/PDF 靜態講義（互動性低、無法切換語言與線上計分）。

**生效版本：**
v2.5.0
