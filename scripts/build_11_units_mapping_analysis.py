import re
import json

with open(r'C:\Users\wu\.gemini\antigravity\brain\29c3fdaf-69e0-4303-b0be-7d6e86b5cbb8\.system_generated\steps\585\content.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract all Units and Lessons from 1727915
units_11 = []
current_unit = None

lines = text.splitlines()
for line in lines:
    clean = re.sub(r'<[^>]+>', '', line).strip()
    if not clean:
        continue
    if '單元' in clean or 'Unit' in clean:
        if current_unit:
            units_11.append(current_unit)
        current_unit = {'name': clean, 'items': []}
    elif current_unit and len(clean) > 2 and not clean.startswith('http'):
        if len(current_unit['items']) < 15:
            current_unit['items'].append(clean)

if current_unit:
    units_11.append(current_unit)

report = "# Google 官方 Level 2 繁體中文 11 個實務單元 (Path 1727915) 完整結構解析\n\n"
for idx, u in enumerate(units_11, 1):
    report += f"## {u['name']}\n"
    for item in u['items']:
        report += f"- {item}\n"
    report += "\n"

with open(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\docs\GCE_Level_2_11個實務單元完整對照表.md', 'w', encoding='utf-8') as f:
    f.write(report)

print("Saved GCE_Level_2_11個實務單元完整對照表.md")
