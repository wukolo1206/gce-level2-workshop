import os

files_to_check = [
    r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\exam_registration.html',
    r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\study_guide_app.html',
    r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\lab_exercises_app.html',
    r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\docs\EXAM_REGISTRATION_GUIDE.md',
    r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\docs\GCE_Level_2_Quiz_A_25題完整考題庫.md'
]

for p in files_to_check:
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if '在控制台進行真實工具操作' in line or 'Classroom Lab' in line:
                    print(f"File: {os.path.basename(p)}, Line {i+1}: {line.strip()}")
                    # print context lines
                    start = max(0, i - 5)
                    end = min(len(lines), i + 8)
                    for j in range(start, end):
                        print(f"  {j+1}: {lines[j].rstrip()}")
                    print("-" * 50)
