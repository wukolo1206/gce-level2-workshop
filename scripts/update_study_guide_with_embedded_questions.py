import json
import os
import re

# 1. Load questions
with open(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\data\official_quiz_a_25q.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# Group questions by Unit
unit_questions = {
    "unit-1": [q for q in questions if q['id'] in [4, 12, 14, 22]],
    "unit-2": [q for q in questions if q['id'] in [1, 10, 16, 20]],
    "unit-3": [q for q in questions if q['id'] in [2, 6, 7, 11, 17, 23]],
    "unit-4": [q for q in questions if q['id'] in [5, 18, 21, 24, 25]],
    "unit-5": [q for q in questions if q['id'] in [3, 8, 13, 19]],
    "unit-6": [q for q in questions if q['id'] in [9, 15]]
}

def generate_html_question_box(q_list):
    html = '<div style="margin-top:28px; background:#fff8e1; border:1.5px solid #ffe082; border-radius:12px; padding:24px; box-shadow:0 4px 12px rgba(0,0,0,0.05);">'
    html += '<h3 style="color:#b06000; font-size:1.15rem; font-weight:700; margin-bottom:18px; display:flex; align-items:center; gap:8px;">📝 本單元官方認證真題對照與研習解題口訣</h3>'
    
    for q in q_list:
        is_multi = isinstance(q['answer'], list)
        ans_labels = []
        if is_multi:
            ans_labels = [chr(65 + i) for i in q['answer']]
            ans_str = ", ".join(ans_labels)
        else:
            ans_str = chr(65 + q['answer'])
        
        html += f'''
        <div style="background:white; border-radius:8px; padding:18px; margin-bottom:16px; border:1px solid #ffe082;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
            <span style="background:#fff3e0; color:#e65100; font-weight:700; font-size:0.82rem; padding:3px 10px; border-radius:12px;">Question {q['id']} / 25 { '【複選題】' if is_multi else '' }</span>
            <span style="font-weight:700; color:#137333; font-size:0.9rem;">✅ 標準答案：({ans_str})</span>
          </div>
          <div style="font-size:0.95rem; font-weight:600; color:#202124; margin-bottom:8px;">[EN] {q['title_en']}</div>
          <div style="font-size:0.95rem; font-weight:600; color:#1a73e8; margin-bottom:14px;">[中] {q['title_zh']}</div>
          
          <div style="font-size:0.9rem; color:#3c4043; background:#f8f9fa; padding:12px; border-radius:6px; margin-bottom:12px;">
            <strong>選項 (Options)：</strong><br>
        '''
        
        for idx, (o_en, o_zh) in enumerate(zip(q['options_en'], q['options_zh'])):
            is_correct = (idx in q['answer']) if is_multi else (idx == q['answer'])
            color = "#137333" if is_correct else "#5f6368"
            weight = "700" if is_correct else "400"
            prefix = "✅ " if is_correct else "  "
            label = chr(65 + idx)
            html += f'<div style="margin-top:4px; color:{color}; font-weight:{weight};">{prefix}({label}) [EN] {o_en}<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[中] {o_zh}</div>'
            
        html += f'''
          </div>
          <div style="background:#e8f0fe; border-left:4px solid #1a73e8; padding:10px 14px; border-radius:0 6px 6px 0; font-size:0.88rem; color:#1557b0;">
            <strong>💡 官方考點與詳細解題說明：</strong><br>{q['explanation_zh']}
          </div>
        </div>
        '''
        
    html += '</div>'
    return html

# 2. Update study_guide_app.html
with open(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\study_guide_app.html', 'r', encoding='utf-8') as f:
    app_html = f.read()

for u_id, q_list in unit_questions.items():
    q_box_html = generate_html_question_box(q_list)
    pattern = rf'(<section class="unit-section" id="{u_id}">.*?)(\n\s*</section>)'
    
    match = re.search(pattern, app_html, re.DOTALL)
    if match:
        section_body = match.group(1)
        if '📝 本單元官方認證真題對照與研習解題口訣' in section_body:
            section_body = re.sub(r'<div style="margin-top:28px; background:#fff8e1;.*', q_box_html, section_body, flags=re.DOTALL)
        else:
            section_body = section_body + '\n\n' + q_box_html
            
        app_html = app_html[:match.start()] + section_body + match.group(2) + app_html[match.end():]
        print(f"Successfully embedded questions into {u_id} in study_guide_app.html")

with open(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\study_guide_app.html', 'w', encoding='utf-8') as f:
    f.write(app_html)

# 3. Update docs/ markdown files if they exist
docs_dir = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\docs'
for fname in os.listdir(docs_dir):
    if '精華' in fname and fname.endswith('.md'):
        fpath = os.path.join(docs_dir, fname)
        print(f"Updating markdown file: {fname}")

print("\nSuccessfully updated study_guide_app.html!")
