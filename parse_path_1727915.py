import re

with open(r'C:\Users\wu\.gemini\antigravity\brain\29c3fdaf-69e0-4303-b0be-7d6e86b5cbb8\.system_generated\steps\585\content.md', 'r', encoding='utf-8') as f:
    html = f.read()

# Clean HTML tags
def clean_html(raw_html):
    cleanr = re.compile('<[^>]+>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

lines = html.splitlines()
parsed = []

for line in lines:
    clean = clean_html(line).strip()
    if clean and len(clean) > 2:
        parsed.append(clean)

output_text = "# Path 1727915 Content Analysis\n\n"
for p in parsed[:200]:
    output_text += p + "\n"

with open(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\path_1727915_parsed.txt', 'w', encoding='utf-8') as f:
    f.write(output_text)

print("Saved path_1727915_parsed.txt")
