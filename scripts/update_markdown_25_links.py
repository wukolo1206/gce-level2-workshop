import json, os

links_path = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\all_25_real_workspace_links.json'
with open(links_path, 'r', encoding='utf-8') as f:
    links = json.load(f)

md_path = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\docs\GCE_Level_2_25個全實作原創教學情境演練手冊.md'
with open(md_path, 'r', encoding='utf-8') as f:
    content = f.read()

for t_num in range(1, 26):
    key = f"Task {t_num:02d}"
    if key in links:
        url = links[key]["url"]
        t_type = links[key]["type"]
        tag = f"#### 演練 {t_num:02d}"
        replacement = f"#### 演練 {t_num:02d}\n> 🔗 **雲端真實線上 {t_type} 實作檔案網址**：[{url}]({url})\n"
        
        # Replace if tag exists and link not already present right below
        if tag in content and url not in content:
            content = content.replace(tag, replacement, 1)

with open(md_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated Markdown guide with ALL 25 REAL LINKS!")
