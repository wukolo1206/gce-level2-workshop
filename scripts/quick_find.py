import os, glob

for p in glob.glob(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\*.html'):
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
        if '在控制台進行真實工具操作' in c or 'Classroom Lab' in c or '選擇板 (Choice boards)' in c:
            print(f"Found in HTML: {p}")

for p in glob.glob(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\docs\*.md'):
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
        if '在控制台進行真實工具操作' in c or 'Classroom Lab' in c or '選擇板 (Choice boards)' in c:
            print(f"Found in MD: {p}")
