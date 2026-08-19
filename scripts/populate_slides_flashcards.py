import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

token_path = r'd:\備課ai\google workspace\token.json'
creds = Credentials.from_authorized_user_file(token_path)
slides_service = build('slides', 'v1', credentials=creds)

presentation_id = '1e4CsXlrX-6XQ8iuBBHtKUaYwmRJ66hpPoQ215IVz-as'

# First get current presentation
pres = slides_service.presentations().get(presentationId=presentation_id).execute()
existing_slides = pres.get('slides', [])

requests = []

# Delete all elements on existing slide 1
slide_1_id = existing_slides[0]['objectId']
for elem in existing_slides[0].get('pageElements', []):
    requests.append({'deleteObject': {'objectId': elem['objectId']}})

# Create 3 more blank slides
slide_2_id = 'slide_word_1'
slide_3_id = 'slide_word_2'
slide_4_id = 'slide_word_3'

# Create slides if not already exist
requests.append({
    'createSlide': {
        'objectId': slide_2_id,
        'insertionIndex': 1,
        'slideLayoutReference': {'predefinedLayout': 'BLANK'}
    }
})
requests.append({
    'createSlide': {
        'objectId': slide_3_id,
        'insertionIndex': 2,
        'slideLayoutReference': {'predefinedLayout': 'BLANK'}
    }
})
requests.append({
    'createSlide': {
        'objectId': slide_4_id,
        'insertionIndex': 3,
        'slideLayoutReference': {'predefinedLayout': 'BLANK'}
    }
})

# Slide 1 Content: Title, Instructions, 3 Word Question Cards
# Helper functions for shapes
def add_textbox(requests, element_id, page_id, text, x, y, w, h, font_size=14, bold=False, color=(0.13, 0.13, 0.14), bg_color=None, border_color=None, align='START'):
    requests.append({
        'createShape': {
            'objectId': element_id,
            'shapeType': 'RECTANGLE',
            'elementProperties': {
                'pageObjectId': page_id,
                'size': {'width': {'magnitude': w, 'unit': 'PT'}, 'height': {'magnitude': h, 'unit': 'PT'}},
                'transform': {'scaleX': 1, 'scaleY': 1, 'translateX': x, 'translateY': y, 'unit': 'PT'}
            }
        }
    })
    if bg_color:
        requests.append({
            'updateShapeProperties': {
                'objectId': element_id,
                'shapeProperties': {
                    'shapeBackgroundFill': {
                        'solidFill': {'color': {'rgbColor': {'red': bg_color[0], 'green': bg_color[1], 'blue': bg_color[2]}}}
                    }
                },
                'fields': 'shapeBackgroundFill.solidFill.color'
            }
        })
    else:
        requests.append({
            'updateShapeProperties': {
                'objectId': element_id,
                'shapeProperties': {'shapeBackgroundFill': {'propertyState': 'NOT_RENDERED'}},
                'fields': 'shapeBackgroundFill'
            }
        })
    
    if border_color:
        requests.append({
            'updateShapeProperties': {
                'objectId': element_id,
                'shapeProperties': {
                    'outline': {
                        'outlineFill': {'solidFill': {'color': {'rgbColor': {'red': border_color[0], 'green': border_color[1], 'blue': border_color[2]}}}},
                        'weight': {'magnitude': 1.5, 'unit': 'PT'}
                    }
                },
                'fields': 'outline'
            }
        })
    else:
        requests.append({
            'updateShapeProperties': {
                'objectId': element_id,
                'shapeProperties': {'outline': {'propertyState': 'NOT_RENDERED'}},
                'fields': 'outline'
            }
        })

    requests.append({
        'insertText': {
            'objectId': element_id,
            'text': text,
            'insertionIndex': 0
        }
    })
    requests.append({
        'updateTextStyle': {
            'objectId': element_id,
            'style': {
                'fontSize': {'magnitude': font_size, 'unit': 'PT'},
                'bold': bold,
                'foregroundColor': {'opaqueColor': {'rgbColor': {'red': color[0], 'green': color[1], 'blue': color[2]}}},
                'fontFamily': 'Google Sans'
            },
            'fields': 'fontSize,bold,foregroundColor,fontFamily'
        }
    })
    if align != 'START':
        requests.append({
            'updateParagraphStyle': {
                'objectId': element_id,
                'style': {'alignment': align},
                'fields': 'alignment'
            }
        })

# 1. Slide 1 elements (Page width: 720pt, height: 405pt in 16:9)
add_textbox(requests, 's1_title', slide_1_id, '🎓 全民英檢中級核心單字 — 互動自習記憶卡', 40, 30, 640, 45, font_size=22, bold=True, color=(0.1, 0.45, 0.91))
add_textbox(requests, 's1_sub', slide_1_id, '自習說明：先看下方單字題目，於心中回想中文意義後，點選「👉 看解答與例句」按鈕跳轉至解答頁！', 40, 78, 640, 28, font_size=12, color=(0.37, 0.39, 0.41))

# Instruction banner for workshop
add_textbox(requests, 's1_inst_box', slide_1_id, '📌【研習實作任務】：請選取下方 3 個按鈕，按右鍵選「連結 (Ctrl+K)」，設定跳轉至本簡報對應的第 2、3、4 頁！', 40, 112, 640, 36, font_size=12, bold=True, color=(0.7, 0.38, 0), bg_color=(1.0, 0.97, 0.88), border_color=(0.98, 0.67, 0))

# Word 1 Card
add_textbox(requests, 's1_card1_bg', slide_1_id, ' 單字 01\n accommodate  (v.)\n [əˋkɑməˌdet]', 40, 160, 195, 180, font_size=15, bold=True, color=(0.1, 0.45, 0.91), bg_color=(0.91, 0.94, 0.99), border_color=(0.1, 0.45, 0.91))
add_textbox(requests, 's1_btn1', slide_1_id, '👉 看解答與例句 (設連結至第2頁)', 48, 290, 179, 40, font_size=11, bold=True, color=(1, 1, 1), bg_color=(0.1, 0.45, 0.91), align='CENTER')

# Word 2 Card
add_textbox(requests, 's1_card2_bg', slide_1_id, ' 單字 02\n collaborate  (v.)\n [kəˋlæbəˌret]', 262, 160, 195, 180, font_size=15, bold=True, color=(0.07, 0.45, 0.2), bg_color=(0.9, 0.96, 0.92), border_color=(0.07, 0.45, 0.2))
add_textbox(requests, 's1_btn2', slide_1_id, '👉 看解答與例句 (設連結至第3頁)', 270, 290, 179, 40, font_size=11, bold=True, color=(1, 1, 1), bg_color=(0.07, 0.45, 0.2), align='CENTER')

# Word 3 Card
add_textbox(requests, 's1_card3_bg', slide_1_id, ' 單字 03\n persevere  (v.)\n [ˌpɝsəˋvɪr]', 484, 160, 195, 180, font_size=15, bold=True, color=(0.48, 0.12, 0.64), bg_color=(0.95, 0.91, 0.99), border_color=(0.48, 0.12, 0.64))
add_textbox(requests, 's1_btn3', slide_1_id, '👉 看解答與例句 (設連結至第4頁)', 492, 290, 179, 40, font_size=11, bold=True, color=(1, 1, 1), bg_color=(0.48, 0.12, 0.64), align='CENTER')

# 2. Slide 2 Content (Word 1: accommodate Answer Page)
add_textbox(requests, 's2_tag', slide_2_id, '📖 單字 01 解答與詳細解析', 40, 30, 640, 30, font_size=14, bold=True, color=(0.1, 0.45, 0.91))
add_textbox(requests, 's2_head', slide_2_id, 'accommodate', 40, 65, 400, 48, font_size=28, bold=True, color=(0.13, 0.13, 0.14))
add_textbox(requests, 's2_phonetic', slide_2_id, '/əˈkɑː.mə.deɪt/  •  動詞 (verb)', 40, 115, 400, 25, font_size=14, color=(0.37, 0.39, 0.41))

add_textbox(requests, 's2_box', slide_2_id, 
'''【核心中文釋義】
1. 容納、提供住宿：為...提供住宿或空間
2. 迎合、使適應：順應某人的需求或配合某種情況

【實用教學例句】
• The new school conference hall can easily accommodate up to 600 teachers and guests.
  （新建的學校會議廳能輕鬆容納多達 600 位教師與貴賓。）
• We will try our best to accommodate the special learning needs of every student.
  （我們將盡全力配合每位學生的特殊學習需求。）''', 
40, 150, 640, 175, font_size=13, color=(0.13, 0.13, 0.14), bg_color=(0.96, 0.97, 0.98), border_color=(0.85, 0.86, 0.88))

# Return button on Slide 2
add_textbox(requests, 's2_return_btn', slide_2_id, '🔙 返回單字目錄題目區 (請設連結回第1頁)', 40, 340, 320, 42, font_size=13, bold=True, color=(1, 1, 1), bg_color=(0.1, 0.45, 0.91), align='CENTER')


# 3. Slide 3 Content (Word 2: collaborate Answer Page)
add_textbox(requests, 's3_tag', slide_3_id, '📖 單字 02 解答與詳細解析', 40, 30, 640, 30, font_size=14, bold=True, color=(0.07, 0.45, 0.2))
add_textbox(requests, 's3_head', slide_3_id, 'collaborate', 40, 65, 400, 48, font_size=28, bold=True, color=(0.13, 0.13, 0.14))
add_textbox(requests, 's3_phonetic', slide_3_id, '/kəˈlæb.ə.reɪt/  •  動詞 (verb)', 40, 115, 400, 25, font_size=14, color=(0.37, 0.39, 0.41))

add_textbox(requests, 's3_box', slide_3_id, 
'''【核心中文釋義】
1. 合作、協作：通常指團隊在專案、學術或研究上共同努力
2. 勾結（在負面語境中）

【實用教學例句】
• Teachers across different grade levels collaborate to design interactive digital learning modules.
  （各年級的教師通力合作，共同設計互動數位學習模組。）
• Google Workspace tools allow students to collaborate on projects in real time.
  （Google Workspace 工具讓學生能夠即時協同合作完成專題。）''', 
40, 150, 640, 175, font_size=13, color=(0.13, 0.13, 0.14), bg_color=(0.96, 0.97, 0.98), border_color=(0.85, 0.86, 0.88))

# Return button on Slide 3
add_textbox(requests, 's3_return_btn', slide_3_id, '🔙 返回單字目錄題目區 (請設連結回第1頁)', 40, 340, 320, 42, font_size=13, bold=True, color=(1, 1, 1), bg_color=(0.07, 0.45, 0.2), align='CENTER')


# 4. Slide 4 Content (Word 3: persevere Answer Page)
add_textbox(requests, 's4_tag', slide_4_id, '📖 單字 03 解答與詳細解析', 40, 30, 640, 30, font_size=14, bold=True, color=(0.48, 0.12, 0.64))
add_textbox(requests, 's4_head', slide_4_id, 'persevere', 40, 65, 400, 48, font_size=28, bold=True, color=(0.13, 0.13, 0.14))
add_textbox(requests, 's4_phonetic', slide_4_id, '/ˌpɝː.səˈvɪr/  •  動詞 (verb)', 40, 115, 400, 25, font_size=14, color=(0.37, 0.39, 0.41))

add_textbox(requests, 's4_box', slide_4_id, 
'''【核心中文釋義】
1. 堅持不懈、不屈不撓：在面臨困難或挑戰時依然持續努力

【實用教學例句】
• If you persevere with your studies and practice every day, you will pass the Level 2 exam.
  （如果你每天堅持研讀並持續練習，你一定能順利通過 Level 2 認證考試。）
• The science club students persevered through failed experiments until they found the solution.
  （科學社團的學生在歷經多次實驗失敗後仍堅持不懈，直到找出解答。）''', 
40, 150, 640, 175, font_size=13, color=(0.13, 0.13, 0.14), bg_color=(0.96, 0.97, 0.98), border_color=(0.85, 0.86, 0.88))

# Return button on Slide 4
add_textbox(requests, 's4_return_btn', slide_4_id, '🔙 返回單字目錄題目區 (請設連結回第1頁)', 40, 340, 320, 42, font_size=13, bold=True, color=(1, 1, 1), bg_color=(0.48, 0.12, 0.64), align='CENTER')

# Execute all batch updates
print(f"Submitting {len(requests)} batch update requests to Slides API...")
response = slides_service.presentations().batchUpdate(
    presentationId=presentation_id,
    body={'requests': requests}
).execute()

print("Successfully populated Google Slides flashcard deck with rich contents!")
