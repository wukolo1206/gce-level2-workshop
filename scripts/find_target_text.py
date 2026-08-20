import os

target = "在控制台進行真實工具操作"
found = []

for root, dirs, files in os.walk(r'd:\備課ai\研習講義'):
    if '.git' in root or '.gh_deploy_temp' in root:
        continue
    for file in files:
        if file.endswith(('.html', '.md', '.json', '.js', '.py')):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if target in content or 'Classroom Lab' in content or '個別分組派發' in content:
                        found.append((filepath, file))
            except Exception as e:
                pass

print("Search results:")
for path, name in found:
    print(f"- {name}: {path}")
