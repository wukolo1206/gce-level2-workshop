import urllib.request
import re
import os
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

activities = [
    {"id": "3306618", "unit": "Unit 1", "title": "Boost your efficiency in Gmail"},
    {"id": "3306619", "unit": "Unit 1", "title": "Explore add-ons in Google Workspace for Education"},
    {"id": "3306620", "unit": "Unit 1", "title": "Level up collaboration with smart canvas"},
    {"id": "3306622", "unit": "Unit 2", "title": "Organize guardian Information with Google Forms"},
    {"id": "3306623", "unit": "Unit 2", "title": "Create a communication system with Google tools"},
    {"id": "3306624", "unit": "Unit 2", "title": "Manage meetings with Google Workspace for Education"},
    {"id": "3306626", "unit": "Unit 3", "title": "Create a digital syllabus in Google Docs"},
    {"id": "3306627", "unit": "Unit 3", "title": "Create digital portfolios with Google Drive and Sites"},
    {"id": "3306629", "unit": "Unit 4", "title": "Deliver interactive presentations with Google Slides"},
    {"id": "3306630", "unit": "Unit 4", "title": "Use Google Meet to Connect to the World"},
    {"id": "3306632", "unit": "Unit 5", "title": "Share personalization options using Google Workspace for Education"},
    {"id": "3306633", "unit": "Unit 5", "title": "Visualize learning using Google Workspace for Education"},
    {"id": "3306634", "unit": "Unit 5", "title": "Publish work online using Google tools"},
    {"id": "3306635", "unit": "Unit 5", "title": "Teaching and learning best practice"},
    {"id": "3306637", "unit": "Unit 6", "title": "Deliver formative assessments with Google Classroom and Forms"},
    {"id": "3306638", "unit": "Unit 6", "title": "Visualize student results with Google Sheets"},
    {"id": "3306639", "unit": "Unit 6", "title": "Analyze data in Google Sheets"},
    {"id": "3306641", "unit": "Assessment", "title": "Test your knowledge in the Intermediate use"}
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

results = []

for act in activities:
    url = f"https://edu.exceedlms.com/student/path/1717663/activity/{act['id']}?locale=zh_tw"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            
            desc_match = re.search(r'<meta name="description" content="(.*?)"', html, re.DOTALL)
            description = desc_match.group(1) if desc_match else ""
            
            paragraphs = re.findall(r'<p[^>]*>(.*?)</p>', html, re.DOTALL)
            clean_paragraphs = [re.sub(r'<[^>]+>', '', p).strip() for p in paragraphs if len(re.sub(r'<[^>]+>', '', p).strip()) > 15]
            
            results.append({
                "id": act["id"],
                "unit": act["unit"],
                "title": act["title"],
                "description": description,
                "paragraphs": clean_paragraphs
            })
            print(f"Successfully fetched [{act['unit']}] {act['title']}")
    except Exception as e:
        print(f"Error fetching {act['id']}: {e}")

out_path = os.path.join(os.path.dirname(__file__), "official_course_dump.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\nSaved all 18 lessons content to {out_path}")
