import os

path_md = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\docs\GCE_Level_2_25個全實作原創教學情境演練手冊.md'
with open(path_md, 'r', encoding='utf-8') as f:
    text = f.read()

old_block = '''#### 演練 14
> 🔗 **雲端真實線上 Slides 實作檔案網址**：[https://docs.google.com/presentation/d/18n8iq45pZ0qDogQYsFkXxp7VGBG14vyQpJtswluGjTs/copy](https://docs.google.com/presentation/d/18n8iq45pZ0qDogQYsFkXxp7VGBG14vyQpJtswluGjTs/copy)
：全校統一簡報母版與圖片預留框 (主題建構工具)
- **🎯 實務情境課題**：為學校團隊製作標準報告簡報，設置統一格式的圖片上傳預留框。
- **🛠️ 指定工具功能**：Google Slides **主題建構工具 (Theme Builder)**
- **▶️ 手把手實操步驟**：
  1. 點選選單「檢視 $\\rightarrow$ 主題建構工具」。
  2. 點選「插入 $\\rightarrow$ 預留位置 $\\rightarrow$ 圖片預留位置 (Image placeholder)」。
- **✨ 成果驗證點**：回到主頁面時出現一鍵點擊上傳圖片的預留框。'''

new_block = '''#### 演練 14
> 🔗 **雲端真實線上 Slides 實作檔案網址**：[https://docs.google.com/presentation/d/18n8iq45pZ0qDogQYsFkXxp7VGBG14vyQpJtswluGjTs/copy](https://docs.google.com/presentation/d/18n8iq45pZ0qDogQYsFkXxp7VGBG14vyQpJtswluGjTs/copy)
：全校統一簡報母版與圖片預留框 (主題製作工具 Theme Builder)

##### 🧩 觀念釐清：母片階層邏輯與「套用版面配置」的對應關係
![主題製作工具母片結構](../images/theme_builder_master_structure.png)
*圖 1：主題製作工具（後台模具工廠：頂部為全域主題母片，下方縮排為各版面配置）*

![套用版面配置選單](../images/apply_layout_templates_menu.png)
*圖 2：前台「套用版面配置」選單（與後台模具工廠一對一完全對應）*

- **👑 1. 最頂端大張【主題母片】（總指揮官）**：定義全校統一字型、背景色、角落校徽 Logo、頁碼。動這 1 張，整份簡報所有頁面自動全部套用！
- **📑 2. 底下縮排的十幾張【版面配置 (Layouts)】（各場景模具）**：針對不同教學場景（封面、內文、雙欄、照片展示）設計模具。新增的「圖片預留位置」，會直接呈現在前台的「套用版面配置」選單中供教師一鍵套用！
- **🛡️ 3. 防呆保護機制**：畫在母片／版面配置中的物件，回到一般編輯模式下點不到、刪不掉，確保格式不被改壞！

- **🎯 實務情境課題**：為學校團隊製作標準報告簡報，設置統一格式的圖片上傳預留框。
- **🛠️ 指定工具功能**：Google Slides **主題製作工具 (Theme Builder)**
- **▶️ 手把手實操步驟**：
  1. 點選選單「查看 ➔ 主題製作工具 (Theme Builder)」。
  2. 點選「插入 ➔ 預留位置 ➔ 圖片預留位置 (Image placeholder)」，先選形狀後拖曳出大小。
  3. 左側縮圖按右鍵重新命名版面配置為 `Image Placeholder`（系統評分逐字比對）。
  4. 點右上角「X」離開主題製作工具，回到一般頁面驗證照片框。
- **✨ 成果驗證點**：回到主頁面時出現一鍵點擊上傳圖片的預留框。'''

if old_block in text:
    text = text.replace(old_block, new_block)
    with open(path_md, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated markdown manual!")
else:
    print("old_block not found in markdown manual, checking lines...")
