# LLM 數位證書客服評估框架

本專案使用 promptfoo 建立統一的 LLM 評估框架，用於測試數位證書客服機器人的回應品質及拒絕非相關問題的能力。

## 專案結構
```
/prompt_alignment
│
├── promptfooconfig.yaml    # 主要配置檔，定義模型、測試和評估方式
├── README.md               # 專案說明文件
├── baseline.json           # 基準測試結果，用於比較模型性能變化
├── promptfoo-errors.log    # 錯誤日誌檔案
│
├── prompts/                # 提示詞模板目錄
│   └── test.json           # 數位證書客服的系統提示，使用 ChatML 格式
│
├── providers/              # 模型提供者配置目錄
│   ├── llama.yaml          # Llama 模型配置
│   ├── breeze.yaml         # Breeze 繁體中文模型配置
│   ├── Llama-3.2-3B-F1.yaml # Llama 3.2 3B F1 推理增強模型配置
│   ├── gpt-4o-mini.yaml    # OpenAI GPT-4o Mini 模型配置
│   └── full_pipeline.yaml  # 腳本 as provider腳本 as provider
│
├── scripts/                # 腳本目錄
│   └── full_pipeline.py    # 端到端處理管道的腳本
│
├── tests/                  # 測試案例目錄
│   ├── test1.py            # 數位證書相關問題測試
│   ├── test2.py            # 非相關問題拒絕測試
│   └── __pycache__/        # Python 快取目錄
│
└── scorers/                # 自定義評分器目錄
    ├── score1.py           # 自定義關鍵詞評分函數
    └── __pycache__/        # Python 快取目錄
```

## 使用方法

### 環境準備

1. **Node.js 環境**
   確保已安裝 Node.js (建議 v14 或更高版本)
   ```bash
   node --version
   ```

2. **安裝 promptfoo**
   ```bash
   npm install -g promptfoo
   ```

3. **設定 Ollama (如使用本地模型)**
   確保 Ollama 服務已啟動並載入所需模型
   ```bash
   ollama list
   # 如需載入模型，例如
   ollama pull llama2
   ollama pull ycchen/breeze-7b-instruct-v1_0
   ```

4. **設定 OpenAI API (如使用 OpenAI 模型)**
   設定環境變數
   ```bash
   # Windows
   set OPENAI_API_KEY=your_api_key

   # Linux/Mac
   export OPENAI_API_KEY=your_api_key
   ```

### 執行評估流程

#### 基本評估
執行所有測試與模型的評估：
```bash
promptfoo eval -c promptfooconfig.yaml
```

#### 保存評估結果
將評估結果保存為 JSON 檔案：
```bash
promptfoo eval -c promptfooconfig.yaml --output results.json
```


#### 除錯
顯示詳細的評估過程與錯誤訊息：
```bash
promptfoo eval -c promptfooconfig.yaml --verbose
```

### 視覺化與分析結果

啟動 Web 介面查看最新評估結果：
```bash
promptfoo view
```

Web 介面功能：
- 查看每個模型在不同測試案例的表現
- 比較不同模型的回應內容
- 分析評估分數與錯誤原因
- 匯出評估報告

### 常見問題排解

1. **找不到模型**
   確認模型名稱是否正確，本地模型是否已下載
   ```bash
   # 檢查本地模型
   ollama list
   ```

2. **評估過程錯誤**
   查看 promptfoo-errors.log 檔案找出錯誤原因
   ```bash
   tail -n 50 promptfoo-errors.log
   ```

3. **未獲得評估結果**
   檢查 providers 目錄中的模型配置是否正確

4. **API 金鑰問題**
   確認環境變數是否正確設定
   ```bash
   echo $OPENAI_API_KEY
   ```

### 完整流程範例

以下是一個完整的流程範例，從安裝到執行及檢視結果：

```bash
# 安裝 promptfoo
npm install -g promptfoo

# 設定環境變數 (如使用 OpenAI)
export OPENAI_API_KEY=your_api_key

# 確認 Ollama 服務 (如使用本地模型)
ollama list

# 執行並儲存結果
promptfoo eval -c promptfooconfig.yaml -o result.json

# 啟動視覺化介面比較結果
promptfoo view
```

## 評估標準

本專案使用多種斷言方式評估模型表現：

1. **相關性評估**：
   - 驗證模型回應是否包含「數位證書」等關鍵詞
   - 使用自定義評分函數檢查特定內容（如「發證」流程）

2. **拒絕能力評估**：
   - 檢查模型是否拒絕回答非相關問題（如水果類問題）
   - 驗證回應中是否包含「不相關」或「無法回答」等短語

3. **品質評估**：
   - 使用 LLM-rubric 進行內容相關性的深層評估
   - 使用 JavaScript 檢查特定條件組合

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
   - 也可以實現 `get_assert()` 函數作為默認評估方法

4. **調整評估標準**
   - 修改測試案例中的斷言類型、權重和閾值
   - 可用斷言類型：icontains、regex、python、javascript、llm-rubric 等
   - 調整權重以強調重要的評估維度

5. **自動化測試流程**
   - 結合 CI/CD 工具如 GitHub Actions
   - 設置定期評估以監控模型性能變化
   - 與基準線比較以檢測退化
