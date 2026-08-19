import json
import re

# Load all 25 questions
with open(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\data\official_quiz_a_25q.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# Group questions by Unit
unit_questions = {
    "Unit 1": [q for q in questions if q['id'] in [4, 12, 14, 22]],
    "Unit 2": [q for q in questions if q['id'] in [1, 10, 16, 20]],
    "Unit 3": [q for q in questions if q['id'] in [2, 6, 7, 11, 17, 23]],
    "Unit 4": [q for q in questions if q['id'] in [5, 18, 21, 24, 25]],
    "Unit 5": [q for q in questions if q['id'] in [3, 8, 13, 19]],
    "Unit 6": [q for q in questions if q['id'] in [9, 15]]
}

print("Question distribution across units:")
for u, qlist in unit_questions.items():
    print(f"  {u}: {len(qlist)} questions -> {[q['id'] for qlist in [qlist] for q in qlist]}")
