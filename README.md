# LLM Prompt 品質測試框架

本專案使用 promptfoo 建立統一的 LLM 評估框架，用於測試繁體中文推文生成能力。

## 專案結構
```
/prompt_alignment
│
├── promptfooconfig.yaml    # 主要配置檔，定義模型、測試和評估方式
├── README.md               # 專案說明文件
├── baseline.json           # 基準測試結果，用於比較模型性能變化
├── promptfoo-errors.log    # 錯誤日誌檔案
│
├── providers/              # 模型提供者配置目錄
│   ├── llama.yaml          # Llama 模型配置
│   ├── breeze.yaml         # Breeze 繁體中文模型配置
│   └── gpt-4o-mini.yaml    # OpenAI GPT-4o Mini 模型配置
│
├── tests/                  # 測試案例目錄
│   ├── test1.py            # 香蕉關鍵詞測試生成器
│   ├── test2.py            # 芭樂關鍵詞測試生成器
│   └── __pycache__/        # Python 快取目錄
│
└── scorers/                # 自定義評分器目錄
    ├── score1.py           # 自定義關鍵詞評分函數
    └── __pycache__/        # Python 快取目錄
```

## 使用方法

### 安裝 promptfoo

```bash
npm i -g promptfoo
```

### 執行測試

```bash
promptfoo eval -c promptfooconfig.yaml
```

如果要保存結果，用 `--output results.json`

如果要 debug，用 `--verbose`

如果要比較 baseline，用 `--baseline baseline.json`

### 視覺化結果

```bash
promptfoo view
```

## 評估標準

TBD

## 擴充方式

1. **添加新模型**
   - 在 `providers/` 目錄中建立新的 YAML 檔案
   - 設定模型 ID、標籤和配置參數
   - 在 `promptfooconfig.yaml` 中引用此檔案

2. **添加新測試案例**
   - 在 `tests/` 目錄中建立新的 Python 檔案
   - 實現 `generate_tests()` 函數返回測試定義列表
   - 在 `promptfooconfig.yaml` 中引用此檔案

3. **自定義評分函數**
   - 在 `scorers/` 目錄中建立新的 Python 檔案
   - 實現評分函數，接收輸出文本和上下文，返回分數
   - 在測試案例中通過 `file://./scorers/your_file.py:function_name` 引用

4. **調整評估標準**
   - 修改測試案例中的斷言類型、權重和閾值
   - 可用斷言類型：icontains、regex、python、javascript、llm-rubric 等
   - 調整權重以強調重要的評估維度

5. **自動化測試流程**
   - 結合 CI/CD 工具如 GitHub Actions
   - 設置定期評估以監控模型性能變化
   - 與基準線比較以檢測退化
