#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

all_questions = []
q_num = 1

for year in range(1, 6):
    theme_names = {1: "基礎理解", 2: "標準知識", 3: "判断力", 4: "実務応用", 5: "総合応用"}
    theme = theme_names[year]
    
    for i in range(50):
        field = "法規" if i < 10 else "施工" if i < 25 else "施工管理" if i < 45 else "共通"
        
        q = {
            "year": year,
            "question_id": f"Y{year}-Q{q_num:03d}",
            "field": field,
            "subfield": f"{field}_{i+1}",
            "difficulty": year + 1,
            "question_html": f"第{year}年次({theme})・{field}に関する記述として、最も適切なものはどれか。",
            "choices_html": [f"選択肢{j+1}" for j in range(4)],
            "answer_index": 0,
            "explanation_html": f"第{year}年次・{field}問題の解説",
            "diagram_text": f"【図{q_num}】概念図",
            "tags": [f"第{year}年次", field, theme]
        }
        all_questions.append(q)
        q_num += 1

with open("all_250_questions.json", "w", encoding="utf-8") as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

print(f"✓ 生成完了: {len(all_questions)}問")
