import re

path = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\quiz_app.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add Quiz A / Quiz B toggle button in the header
old_header_controls = '''      <div class="lang-selector">
        <button class="lang-btn active" id="btn-zh" onclick="setLanguage('zh')">繁體中文</button>
        <button class="lang-btn" id="btn-en" onclick="setLanguage('en')">English</button>
        <button class="lang-btn" id="btn-bi" onclick="setLanguage('bi')">中英對照</button>
      </div>'''

new_header_controls = '''      <div style="display:flex; gap:10px; align-items:center; flex-wrap:wrap;">
        <div class="lang-selector" style="background:rgba(255,255,255,0.25);">
          <button class="lang-btn active" id="btn-quiz-a" onclick="switchQuizMode('a')">📘 測驗 A 卷</button>
          <button class="lang-btn" id="btn-quiz-b" onclick="switchQuizMode('b')">📗 測驗 B 卷</button>
        </div>
        <div class="lang-selector">
          <button class="lang-btn active" id="btn-zh" onclick="setLanguage('zh')">繁體中文</button>
          <button class="lang-btn" id="btn-en" onclick="setLanguage('en')">English</button>
          <button class="lang-btn" id="btn-bi" onclick="setLanguage('bi')">中英對照</button>
        </div>
      </div>'''

html = html.replace(old_header_controls, new_header_controls)

# Update JavaScript to support Quiz A / Quiz B dataset switching
old_script_start = '''    let rawQuestions = [];
    let currentFilter = 'all';
    let currentLang = 'zh';
    let userAnswers = {};

    async function fetchQuestions() {
      try {
        const response = await fetch('data/official_quiz_a_25q.json');
        rawQuestions = await response.json();
        renderQuestions();
      } catch (err) {
        console.error('Failed to load questions:', err);
      }
    }

    fetchQuestions();'''

new_script_start = '''    let rawQuestions = [];
    let currentQuiz = 'a';
    let currentFilter = 'all';
    let currentLang = 'zh';
    let userAnswers = {};

    async function fetchQuestions(mode = 'a') {
      try {
        currentQuiz = mode;
        const file = mode === 'b' ? 'data/official_quiz_b_25q.json' : 'data/official_quiz_a_25q.json';
        const response = await fetch(file);
        rawQuestions = await response.json();
        userAnswers = {};
        
        document.getElementById('btn-quiz-a').classList.toggle('active', mode === 'a');
        document.getElementById('btn-quiz-b').classList.toggle('active', mode === 'b');
        
        renderQuestions();
      } catch (err) {
        console.error('Failed to load questions:', err);
      }
    }

    function switchQuizMode(mode) {
      fetchQuestions(mode);
    }

    fetchQuestions('a');'''

html = html.replace(old_script_start, new_script_start)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully upgraded quiz_app.html with Quiz A / Quiz B switching!")
