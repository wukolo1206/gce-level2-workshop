import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

token_path = r'd:\備課ai\google workspace\token.json'
creds = Credentials.from_authorized_user_file(token_path)
slides_service = build('slides', 'v1', credentials=creds)

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

# --- TASK 14: 學校簡報標準母版 ---
pid_14 = '18n8iq45pZ0qDogQYsFkXxp7VGBG14vyQpJtswluGjTs'
pres_14 = slides_service.presentations().get(presentationId=pid_14).execute()
reqs_14 = []
for elem in pres_14.get('slides', [])[0].get('pageElements', []):
    reqs_14.append({'deleteObject': {'objectId': elem['objectId']}})

s1_14 = pres_14.get('slides', [])[0]['objectId']
s2_14 = 't14_slide_2'
s3_14 = 't14_slide_3'
reqs_14.append({'createSlide': {'objectId': s2_14, 'insertionIndex': 1, 'slideLayoutReference': {'predefinedLayout': 'BLANK'}}})
reqs_14.append({'createSlide': {'objectId': s3_14, 'insertionIndex': 2, 'slideLayoutReference': {'predefinedLayout': 'BLANK'}}})

# Slide 1: Cover
add_textbox(reqs_14, 't14_s1_title', s1_14, '🏫 校本課程推動與跨領域教學成果報告', 50, 80, 620, 60, font_size=26, bold=True, color=(0.1, 0.45, 0.91))
add_textbox(reqs_14, 't14_s1_sub', s1_14, '全校標準簡報母版範例 ‧ 教務處編製', 50, 150, 620, 30, font_size=15, color=(0.37, 0.39, 0.41))
add_textbox(reqs_14, 't14_s1_inst', s1_14, '📌【演練目標】：請點選選單「檢視 ➔ 主題製作工具 (Theme Builder)」，建立全校統一母版與「圖片預留位置 (Image placeholder)」！', 50, 220, 620, 60, font_size=13, bold=True, color=(0.7, 0.38, 0), bg_color=(1.0, 0.97, 0.88), border_color=(0.98, 0.67, 0))

# Slide 2: Photo Layout
add_textbox(reqs_14, 't14_s2_head', s2_14, '📸 教學活動紀錄與學生探究剪影', 50, 40, 620, 40, font_size=20, bold=True, color=(0.13, 0.13, 0.14))
add_textbox(reqs_14, 't14_s2_box', s2_14, '【版面說明】\n本頁面需要規範教師放置教學現場照片的位置。\n請至主題製作工具中，為此版面配置新增標準的「圖片預留位置」，確保全校簡報格式統一。', 50, 100, 620, 100, font_size=14, color=(0.2, 0.2, 0.2), bg_color=(0.96, 0.97, 0.98), border_color=(0.85, 0.86, 0.88))

# Slide 3: Conclusion
add_textbox(reqs_14, 't14_s3_head', s3_14, '🎯 展望與致謝', 50, 80, 620, 50, font_size=24, bold=True, color=(0.07, 0.45, 0.2))
add_textbox(reqs_14, 't14_s3_text', s3_14, '感謝全體教學團隊與行政同仁的辛勞與協作！\n透過統一主題母版，大幅節省全校教師製作簡報之排版時間。', 50, 150, 620, 80, font_size=15, color=(0.3, 0.3, 0.3))

slides_service.presentations().batchUpdate(presentationId=pid_14, body={'requests': reqs_14}).execute()
print("Populated Task 14!")


# --- TASK 15: 校園植物導覽簡報 ---
pid_15 = '1QWGOhuKITGsc3mFlbap-VlGFsAvBm0_Y1utRgPM5E2c'
pres_15 = slides_service.presentations().get(presentationId=pid_15).execute()
reqs_15 = []
for elem in pres_15.get('slides', [])[0].get('pageElements', []):
    reqs_15.append({'deleteObject': {'objectId': elem['objectId']}})

s1_15 = pres_15.get('slides', [])[0]['objectId']
s2_15 = 't15_slide_2'
s3_15 = 't15_slide_3'
reqs_15.append({'createSlide': {'objectId': s2_15, 'insertionIndex': 1, 'slideLayoutReference': {'predefinedLayout': 'BLANK'}}})
reqs_15.append({'createSlide': {'objectId': s3_15, 'insertionIndex': 2, 'slideLayoutReference': {'predefinedLayout': 'BLANK'}}})

# Slide 1: Cover
add_textbox(reqs_15, 't15_s1_title', s1_15, '🌿 校園生態導覽 — 臺灣原生水生植物專題', 50, 80, 620, 60, font_size=26, bold=True, color=(0.07, 0.45, 0.2))
add_textbox(reqs_15, 't15_s1_sub', s1_15, '自然與生活科技領域 ‧ 戶外生態池探究學習', 50, 150, 620, 30, font_size=15, color=(0.37, 0.39, 0.41))
add_textbox(reqs_15, 't15_s1_inst', s1_15, '📌【演練目標】：請在第 2 頁點選「插入 ➔ 影片」內嵌 YouTube 影音，並選取影片新增批註「+同仁Email」勾選指派任務！', 50, 220, 620, 60, font_size=13, bold=True, color=(0.7, 0.38, 0), bg_color=(1.0, 0.97, 0.88), border_color=(0.98, 0.67, 0))

# Slide 2: Video insertion page
add_textbox(reqs_15, 't15_s2_head', s2_15, '🎬 臺灣萍蓬草生態觀察紀錄影片', 50, 30, 620, 40, font_size=20, bold=True, color=(0.13, 0.13, 0.14))
add_textbox(reqs_15, 't15_s2_box', s2_15, '【實作操作區】：\n1. 請點選頂部功能表「插入 ➔ 影片 (Insert video)」\n2. 搜尋「臺灣萍蓬草」並插入 YouTube 影片\n3. 選取插入後的影片，在右側新增註解輸入「+夥伴Email」並勾選「指派給...」！', 50, 80, 620, 110, font_size=13, color=(0.13, 0.13, 0.14), bg_color=(0.95, 0.98, 0.95), border_color=(0.5, 0.8, 0.5))

# Slide 3: Discussion
add_textbox(reqs_15, 't15_s3_head', s3_15, '📝 小組探究討論問題', 50, 50, 620, 40, font_size=20, bold=True, color=(0.1, 0.45, 0.91))
add_textbox(reqs_15, 't15_s3_box', s3_15, '1. 臺灣萍蓬草的葉片結構如何適應水生環境？\n2. 校園生態池水質對水生植物生長有何影響？\n3. 請各組完成影片觀賞後，於 Classroom 繳交討論筆記。', 50, 100, 620, 180, font_size=14, color=(0.2, 0.2, 0.2), bg_color=(0.96, 0.97, 0.98), border_color=(0.85, 0.86, 0.88))

slides_service.presentations().batchUpdate(presentationId=pid_15, body={'requests': reqs_15}).execute()
print("Populated Task 15!")
