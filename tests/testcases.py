import pandas as pd

def generate_tests():
    testcases = []
    df = pd.read_csv("data/testcases.csv")
    for index, row in df.iterrows():
        testcases.append({
            "vars": {
                "user_prompt": row["使用者輸入"]
            },
            "assert": [
                {
                    "type": "llm-rubric",
                    "value": row["預期 LLM 回應"],
                    "weight": 1,
                    "provider": "openai:gpt-4o-mini"
                }
            ],
            "threshold": 0.7
        })

    return testcases




    