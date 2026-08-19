import os

path_app = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\docs_workshop_app.html'
with open(path_app, 'r', encoding='utf-8') as f:
    text = f.read()

old_step = '移至文件開頭的第一頁，點選選單 <strong>「插入 $\\rightarrow$ 目錄 (Table of Contents)」</strong>。'
new_step = '移至文件開頭，點選選單 <strong>「插入 $\\rightarrow$ 往下拉到最底部 $\\rightarrow$ 目錄 (Table of Contents)」</strong>（或點選「檢視 $\\rightarrow$ 顯示大綱」開啟左側動態大綱）。'

if old_step in text:
    text = text.replace(old_step, new_step)
    with open(path_app, 'w', encoding='utf-8') as f:
        f.write(text)

path_tasks = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\hands_on_tasks_app.html'
with open(path_tasks, 'r', encoding='utf-8') as f:
    t_text = f.read()

old_t_step = '移至文件開頭，點選選單「插入 -> 目錄 (Table of Contents)」。'
new_t_step = '移至文件開頭，點選選單「插入 -> 往下拉至最底部 -> 目錄 (Table of Contents)」（或點選「檢視 -> 顯示大綱」）。'

if old_t_step in t_text:
    t_text = t_text.replace(old_t_step, new_t_step)
    with open(path_tasks, 'w', encoding='utf-8') as f:
        f.write(t_text)

print("Updated TOC UI tip in both Web Apps!")
