def generate_tests():
    return [
        {
            "vars": {
                "prompt": "用繁體中文寫一則介紹你自己，需要包含「芭樂」這個詞，並且字數在 15 到 60 字之間。"
            },
            "assert": [
                { "type": "icontains", "value": "芭樂",  "weight": 3 },
                { 
                    "type": "python", 
                    "value": "file://./scorers/score1.py", # 沒有 :{FUNCTION}，會自動用 get_assert
                    "weight": 2,
                    "config": {
                        "keyword": "芭樂"
                    }
                },
                { "type": "llm-rubric", "value": "是否跟芭樂有關",  "weight": 1 },
            ],
            "description": "幽默芭樂 Tweet",
        }
    ]