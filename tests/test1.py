def generate_tests():
    return [
        {
            "vars": {
                # promptfoo 若找不到 `prompts:` 會自動用 {{prompt}} 作「直通模板」
                "prompt": "用繁體中文寫一則介紹你自己，需要包含「香蕉」這個詞，並且字數在 15 到 60 字之間。"
            },
            "assert": [
                { "type": "icontains", "value": "香蕉",  "weight": 3 },
                { 
                    "type": "python", 
                    "value": "file://./scorers/score1.py:score", 
                    "weight": 2,
                    "config":  # 用這個 input args, 進去函示後用 context.get("config", {}).get({ARG_NAME}, {DEFAULT_ARG})
                        {"keyword": "香蕉"}
                },
            ],
            "description": "幽默香蕉 Tweet",
        }
    ]