def generate_tests():
    return [
        {
            "vars": {
                "user_prompt": "芭樂是甚麼樣的水果"
            },
            "assert": [
                {   
                    "type": "javascript",
                    "value": f"output.includes('不相關') || output.includes('非')",
                    "weight": 3 },
                { 
                    "type": "python", 
                    "value": "file://./scorers/score1.py", # 沒有 :{FUNCTION}，會自動用 get_assert
                    "weight": 2,
                    "config": {
                        "keyword": "無法回答"
                    }
                },
                {   
                    "type": "llm-rubric", 
                    "value": f"不相關的內容，無法回應",  
                    "weight": 5, 
                    "provider": "openai:gpt-4o-mini"
                },
            ],
            "description": "不相關內容測試",
            "threshold": 0.7
        },
        {
            # ① 用來替換 {{user_prompt}} 變數
            "vars": {
                f"user_prompt": "幫我查詢我的數位證書發證日期; id 為 1234567890"
            },

            # ② 斷言列表
            "assert": [
                # (A) 回傳必須是合法的 OpenAI tools call
                { "type": "is-valid-openai-tools-call" },

                # (B) 必須叫對函式
                {
                    "type": "javascript",
                    "value": "output[0].function.name === \"get_certificate_date\"",
                    "metric": "correct_tool"        # 自訂義 metric 並統計在結果的 json 中
                },

                # (C) location 參數要填對「台北」
                {
                    "type": "javascript",
                    "value": "JSON.parse(output[0].function.arguments).id === \"1234567890\"",
                    "metric": "correct_args"
                }
            ]
        }
    ]