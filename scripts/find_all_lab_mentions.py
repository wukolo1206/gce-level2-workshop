import os, glob

target_files = []
for root, dirs, files in os.walk(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包'):
    if '.git' in root or '.gh_deploy_temp' in root:
        continue
    for file in files:
        if file.endswith(('.html', '.md')):
            p = os.path.join(root, file)
            with open(p, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                if '在控制台進行真實工具操作' in content or 'Classroom Lab' in content or 'Lab Exams' in content:
                    target_files.append(p)

print("Found files to update:")
for f in target_files:
    print(f"- {f}")
