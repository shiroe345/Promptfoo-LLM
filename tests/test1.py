def generate_tests():
    return [
        {
            "vars": {
                # promptfoo 若找不到 `prompts:` 會自動用 {{prompt}} 作「直通模板」
                # "prompt": "{{test-prompt}}",
                "user_prompt": "用繁體中文介紹數位證書的發證流程是如何進行的。"
            },
            "assert": [
                { "type": "icontains", "value": "數位證書",  "weight": 3 },
                { 
                    "type": "python", 
                    "value": "file://./scorers/scoring.py:score", 
                    "weight": 2,
                    "config":  # 用這個 input args, 進去函示後用 context.get("config", {}).get({ARG_NAME}, {DEFAULT_ARG})
                        {"keyword": "發證"}
                },
            ],
            "description": "數位證書發證流程",
        }
    ]