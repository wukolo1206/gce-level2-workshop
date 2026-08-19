import json

with open(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\official_quiz_a_25q.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

json_str = json.dumps(questions, ensure_ascii=False, indent=2)

html_code = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Google Certified Educator Level 2 官方 25 題線上模擬刷題 App (GCE 第 2 級：測驗 A)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&family=Noto+Sans+TC:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary: #1a73e8;
      --primary-dark: #1557b0;
      --accent: #34a853;
      --warning: #fbbc04;
      --danger: #ea4335;
      --dark: #202124;
      --light-bg: #f8f9fa;
      --border: #dadce0;
      --text: #3c4043;
      --text-muted: #5f6368;
      --shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
      --radius: 12px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Noto Sans TC', 'Outfit', sans-serif; }}

    body {{ background: var(--light-bg); color: var(--text); padding-bottom: 60px; }}

    header {{
      background: linear-gradient(135deg, #1a73e8 0%, #0d47a1 100%);
      color: white;
      padding: 24px 32px;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 4px 20px rgba(26, 115, 232, 0.3);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
    }}

    .brand-title h1 {{ font-size: 1.4rem; font-weight: 700; }}
    .brand-title p {{ font-size: 0.88rem; opacity: 0.9; }}

    .lang-switcher {{
      display: flex;
      background: rgba(255,255,255,0.2);
      padding: 4px;
      border-radius: 20px;
      gap: 4px;
    }}

    .lang-btn {{
      border: none;
      background: transparent;
      color: white;
      padding: 6px 14px;
      border-radius: 16px;
      font-weight: 600;
      cursor: pointer;
      font-size: 0.85rem;
      transition: all 0.2s;
    }}

    .lang-btn.active {{ background: white; color: var(--primary); }}

    .container {{ max-width: 960px; margin: 24px auto; padding: 0 16px; }}

    .dashboard-card {{
      background: white;
      border-radius: var(--radius);
      padding: 20px 24px;
      box-shadow: var(--shadow);
      margin-bottom: 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
    }}

    .stat-item {{ text-align: center; flex: 1; min-width: 120px; }}
    .stat-val {{ font-size: 1.8rem; font-weight: 700; color: var(--primary); }}
    .stat-label {{ font-size: 0.85rem; color: var(--text-muted); }}

    .filter-bar {{
      display: flex;
      gap: 8px;
      margin-bottom: 20px;
      overflow-x: auto;
      padding-bottom: 8px;
    }}

    .filter-chip {{
      border: 1px solid var(--border);
      background: white;
      padding: 8px 16px;
      border-radius: 20px;
      font-size: 0.9rem;
      color: var(--text-muted);
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s;
    }}

    .filter-chip.active {{ background: var(--primary); color: white; border-color: var(--primary); }}

    .question-card {{
      background: white;
      border-radius: var(--radius);
      padding: 28px;
      margin-bottom: 20px;
      box-shadow: var(--shadow);
      border-left: 5px solid var(--primary);
    }}

    .q-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
    }}

    .q-tag {{ background: #e8f0fe; color: var(--primary); padding: 4px 10px; border-radius: 6px; font-size: 0.82rem; font-weight: 600; }}
    .q-num {{ font-weight: 700; color: var(--text-muted); font-size: 0.9rem; }}
    
    .q-title {{ font-size: 1.12rem; font-weight: 600; color: var(--dark); margin-bottom: 18px; line-height: 1.6; }}

    .options {{ display: flex; flex-direction: column; gap: 10px; }}

    .option-btn {{
      display: flex;
      align-items: flex-start;
      padding: 14px 18px;
      border: 1.5px solid var(--border);
      border-radius: 8px;
      background: white;
      cursor: pointer;
      text-align: left;
      font-size: 0.95rem;
      transition: all 0.2s;
    }}

    .option-btn:hover {{ background: #f8f9fa; border-color: var(--primary); }}
    .option-btn.correct {{ background: #e6f4ea; border-color: var(--accent); color: #137333; font-weight: 600; }}
    .option-btn.wrong {{ background: #fce8e6; border-color: var(--danger); color: #c5221f; }}

    .opt-label {{ font-weight: 700; margin-right: 10px; min-width: 24px; }}

    .explanation-box {{
      margin-top: 18px;
      padding: 16px;
      border-radius: 8px;
      background: #e8f0fe;
      border-left: 4px solid var(--primary);
      display: none;
      font-size: 0.92rem;
      line-height: 1.6;
    }}

    .submit-multi-btn {{
      margin-top: 14px;
      padding: 10px 20px;
      background: var(--primary);
      color: white;
      border: none;
      border-radius: 6px;
      font-weight: 700;
      cursor: pointer;
    }}

    @media (max-width: 600px) {{
      header {{ padding: 16px; }}
      .container {{ padding: 12px; }}
    }}
  </style>
</head>
<body>

  <header>
    <div class="brand-title">
      <h1>Google Certified Educator Level 2 真題刷題系統</h1>
      <p>收錄 GCE 第 2 級：測驗 A (Quiz A) 完整 25 題實務真題與中英雙語切換</p>
    </div>
    <div class="lang-switcher">
      <button class="lang-btn active" id="lang-zh" onclick="setGlobalLang('zh')">繁體中文</button>
      <button class="lang-btn" id="lang-en" onclick="setGlobalLang('en')">English</button>
      <button class="lang-btn" id="lang-bi" onclick="setGlobalLang('bi')">中英對照</button>
    </div>
  </header>

  <div class="container">
    
    <div class="dashboard-card">
      <div class="stat-item">
        <div class="stat-val" id="total-count">25</div>
        <div class="stat-label">總題數</div>
      </div>
      <div class="stat-item">
        <div class="stat-val" id="answered-count">0</div>
        <div class="stat-label">已答題數</div>
      </div>
      <div class="stat-item">
        <div class="stat-val" id="score-count" style="color:var(--accent);">0 / 25</div>
        <div class="stat-label">得分狀況</div>
      </div>
    </div>

    <div class="filter-bar">
      <button class="filter-chip active" onclick="filterCategory('all')">全選 (25 題)</button>
      <button class="filter-chip" onclick="filterCategory('Unit 1')">Unit 1: 行政與自動化</button>
      <button class="filter-chip" onclick="filterCategory('Unit 2')">Unit 2: 親師與跨校溝通</button>
      <button class="filter-chip" onclick="filterCategory('Unit 3')">Unit 3: 班級素材與平台</button>
      <button class="filter-chip" onclick="filterCategory('Unit 4')">Unit 4: 互動簡報與會議</button>
      <button class="filter-chip" onclick="filterCategory('Unit 5')">Unit 5: 個人化差異學習</button>
      <button class="filter-chip" onclick="filterCategory('Unit 6')">Unit 6: 數據與評量分析</button>
    </div>

    <div id="questions-list"></div>

  </div>

  <script>
    const rawQuestions = {json_str};

    let currentLang = 'zh';
    let userAnswers = {{}};
    let currentFilter = 'all';

    function setGlobalLang(lang) {{
      currentLang = lang;
      document.querySelectorAll('.lang-btn').forEach(b => b.classList.remove('active'));
      document.getElementById('lang-' + lang).classList.add('active');
      renderQuestions();
    }}

    function filterCategory(cat) {{
      currentFilter = cat;
      document.querySelectorAll('.filter-chip').forEach(b => b.classList.remove('active'));
      event.currentTarget.classList.add('active');
      renderQuestions();
    }}

    function renderQuestions() {{
      const container = document.getElementById('questions-list');
      container.innerHTML = '';

      const filtered = rawQuestions.filter(q => {{
        if (currentFilter === 'all') return true;
        return q.unit.includes(currentFilter);
      }});

      document.getElementById('total-count').innerText = filtered.length;

      filtered.forEach((q, idx) => {{
        const card = document.createElement('div');
        card.className = 'question-card';

        let titleText = '';
        if (currentLang === 'zh') titleText = q.title_zh;
        else if (currentLang === 'en') titleText = q.title_en;
        else titleText = '<div style="margin-bottom:8px;"><strong>[EN]</strong> ' + q.title_en + '</div><div><strong>[中]</strong> ' + q.title_zh + '</div>';

        const isMulti = Array.isArray(q.answer);

        let html = `
          <div class="q-header">
            <span class="q-tag">${{q.unit}} ${{isMulti ? '【複選題】' : ''}}</span>
            <span class="q-num">Question ${{q.id}} / 25</span>
          </div>
          <div class="q-title">${{titleText}}</div>
          <div class="options" id="opts-${{q.id}}">
        `;

        q.options_zh.forEach((optZh, optIdx) => {{
          const optEn = q.options_en[optIdx];
          let optText = '';
          if (currentLang === 'zh') optText = optZh;
          else if (currentLang === 'en') optText = optEn;
          else optText = '<div><strong>[EN]</strong> ' + optEn + '</div><div style="font-size:0.88rem; color:#5f6368;"><strong>[中]</strong> ' + optZh + '</div>';

          const label = String.fromCharCode(65 + optIdx);

          html += `
            <button class="option-btn" id="opt-${{q.id}}-${{optIdx}}" onclick="handleSelect(${{q.id}}, ${{optIdx}}, ${{isMulti}})">
              <span class="opt-label">${{label}}.</span>
              <div>${{optText}}</div>
            </button>
          `;
        }});

        html += `</div>`;

        if (isMulti) {{
          html += `<button class="submit-multi-btn" onclick="checkMultiAnswer(${{q.id}})">確認提交複選答案</button>`;
        }}

        html += `
          <div class="explanation-box" id="exp-${{q.id}}">
            <strong>💡 官方考點與詳細說明：</strong><br>
            ${{q.explanation_zh}}
          </div>
        `;

        card.innerHTML = html;
        container.appendChild(card);

        if (userAnswers[q.id]) {{
          restoreState(q.id, isMulti);
        }}
      }});

      updateStats();
    }}

    function handleSelect(qid, optIdx, isMulti) {{
      if (isMulti) {{
        if (!userAnswers[qid]) userAnswers[qid] = [];
        const pos = userAnswers[qid].indexOf(optIdx);
        if (pos > -1) userAnswers[qid].splice(pos, 1);
        else userAnswers[qid].push(optIdx);

        document.querySelectorAll(`#opts-${{qid}} .option-btn`).forEach((btn, idx) => {{
          if (userAnswers[qid].includes(idx)) btn.style.borderColor = 'var(--primary)';
          else btn.style.borderColor = 'var(--border)';
        }});
      }} else {{
        userAnswers[qid] = optIdx;
        const q = rawQuestions.find(item => item.id === qid);
        const correct = q.answer;

        document.querySelectorAll(`#opts-${{qid}} .option-btn`).forEach((btn, idx) => {{
          btn.disabled = true;
          if (idx === correct) btn.classList.add('correct');
          if (idx === optIdx && idx !== correct) btn.classList.add('wrong');
        }});

        document.getElementById('exp-' + qid).style.display = 'block';
        updateStats();
      }}
    }}

    function checkMultiAnswer(qid) {{
      const q = rawQuestions.find(item => item.id === qid);
      const correctArr = q.answer;
      const userArr = userAnswers[qid] || [];

      document.querySelectorAll(`#opts-${{qid}} .option-btn`).forEach((btn, idx) => {{
        btn.disabled = true;
        if (correctArr.includes(idx)) btn.classList.add('correct');
        if (userArr.includes(idx) && !correctArr.includes(idx)) btn.classList.add('wrong');
      }});

      document.getElementById('exp-' + qid).style.display = 'block';
      updateStats();
    }}

    function restoreState(qid, isMulti) {{
      const q = rawQuestions.find(item => item.id === qid);
      const correct = q.answer;
      const userAns = userAnswers[qid];

      if (isMulti) {{
        document.querySelectorAll(`#opts-${{qid}} .option-btn`).forEach((btn, idx) => {{
          btn.disabled = true;
          if (correct.includes(idx)) btn.classList.add('correct');
          if (Array.isArray(userAns) && userAns.includes(idx) && !correct.includes(idx)) btn.classList.add('wrong');
        }});
      }} else {{
        document.querySelectorAll(`#opts-${{qid}} .option-btn`).forEach((btn, idx) => {{
          btn.disabled = true;
          if (idx === correct) btn.classList.add('correct');
          if (idx === userAns && idx !== correct) btn.classList.add('wrong');
        }});
      }}
      document.getElementById('exp-' + qid).style.display = 'block';
    }}

    function updateStats() {{
      const answered = Object.keys(userAnswers).length;
      document.getElementById('answered-count').innerText = answered;

      let score = 0;
      Object.keys(userAnswers).forEach(qidStr => {{
        const qid = parseInt(qidStr);
        const q = rawQuestions.find(item => item.id === qid);
        const uAns = userAnswers[qid];

        if (Array.isArray(q.answer)) {{
          if (Array.isArray(uAns) && uAns.sort().join(',') === q.answer.sort().join(',')) {{
            score++;
          }}
        }} else {{
          if (uAns === q.answer) score++;
        }}
      }});

      document.getElementById('score-count').innerText = score + ' / ' + rawQuestions.length;
    }}

    window.onload = renderQuestions;
  </script>
</body>
</html>
"""

with open(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\quiz_app.html', 'w', encoding='utf-8') as f:
    f.write(html_code)

print('Successfully created quiz_app.html with all 25 questions and language toggle!')
