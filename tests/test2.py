def generate_tests():
    return [
        {
            "vars": {
                "user_prompt": "芭樂是甚麼樣的水果"
            },
            "assert": [
                {   
                    "type": "javascript",
                    "value": "output.includes('不相關') || output.includes('非')",
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
                    "value": "不相關的內容，無法回應",  
                    "weight": 5, 
                    "provider": "openai:gpt-4o-mini"
                },
            ],
            "description": "不相關內容測試",
            "threshold": 0.7
        }
    ]