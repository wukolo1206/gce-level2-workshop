import os

real_link = "https://docs.google.com/document/d/1kE7fdTcA9Po3xXxpHmt-iaC1EQtKI0QVuEN8HhnQcXE/edit?usp=sharing"

# Update docs/Google_Docs_進階功能與行政自動化研習講義.md
path1 = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\docs\Google_Docs_進階功能與行政自動化研習講義.md'
with open(path1, 'r', encoding='utf-8') as f:
    text1 = f.read()

link_md = f"""\n> 🔗 **線上真實 Google Docs 實作檔連結**：  
> 📄 **[{real_link}]({real_link})**  
> （點選開啟即可直接在文件內按下 `Ctrl + H`，將舊校長姓名 `陳大文` 一鍵取代為 `張小明`！）\n"""

if real_link not in text1:
    text1 = text1.replace('### 1. 尋找與取代 (Find and Replace)', '### 1. 尋找與取代 (Find and Replace)\n' + link_md)
    with open(path1, 'w', encoding='utf-8') as f:
        f.write(text1)

# Update docs/GCE_Level_2_25個全實作原創教學情境演練手冊.md
path2 = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\docs\GCE_Level_2_25個全實作原創教學情境演練手冊.md'
with open(path2, 'r', encoding='utf-8') as f:
    text2 = f.read()

if real_link not in text2:
    text2 = text2.replace('#### 演練 01：全校週報校長姓名全篇快速更正 (取代工具)', '#### 演練 01：全校週報校長姓名全篇快速更正 (取代工具)\n' + link_md)
    with open(path2, 'w', encoding='utf-8') as f:
        f.write(text2)

print("Updated Markdown files with real link!")
