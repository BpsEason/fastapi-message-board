# 留言系統 API

這是一個使用 Python 和 FastAPI 開發的簡單留言系統 RESTful API，適合 Python 初學者學習 Web 後端開發。專案包含留言的創建、讀取、更新和刪除 (CRUD) 功能，使用 SQLite 作為資料庫。

## 功能

- **創建留言**：發送 POST 請求到 `/messages/`，包含作者和內容。
- **獲取所有留言**：發送 GET 請求到 `/messages/`，按創建時間降序排列。
- **獲取單一留言**：發送 GET 請求到 `/messages/{id}`，根據 ID 查詢。
- **更新留言**：發送 PUT 請求到 `/messages/{id}`，修改作者或內容。
- **刪除留言**：發送 DELETE 請求到 `/messages/{id}`，刪除指定留言。

## 技術棧

- **Python 3.8+**：程式語言
- **FastAPI**：高效的 Web 框架，支援異步處理
- **SQLite**：輕量級資料庫，無需額外伺服器
- **Pydantic**：數據驗證和型別檢查
- **python-dotenv**：環境變數管理

## 專案結構

```
├── main.py           # 主應用程式，包含 API 端點和資料庫邏輯
├── tests.py         # 測試程式碼，使用 pytest 進行單元測試
├── requirements.txt # 依賴清單
├── .env.example     # 環境變數範例
├── .gitignore       # Git 忽略檔案清單
└── README.md        # 專案說明文件
```

## 安裝與運行

1. **克隆專案**：
   ```bash
   git clone https://github.com/your-username/message-board-api.git
   cd message-board-api
   ```

2. **創建虛擬環境（可選）**：
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows 使用 .venv\Scripts\activate
   ```

3. **安裝依賴**：
   ```bash
   pip install -r requirements.txt
   ```

4. **配置環境變數**：
   複製 `.env.example` 為 `.env`：
   ```bash
   cp .env.example .env
   ```
   根據需要修改 `.env` 中的 `DB_PATH` 和 `PORT`。

5. **運行應用**：
   ```bash
   python main.py
   ```

6. **訪問 API 文件**：
   開啟瀏覽器，訪問 `http://localhost:8000/docs`，使用 Swagger UI 測試 API。

## 測試

專案包含基本的單元測試，使用 `pytest` 和 `httpx`。

1. 安裝測試依賴：
   ```bash
   pip install pytest httpx
   ```

2. 運行測試：
   ```bash
   pytest tests.py
   ```

## 環境變數

在 `.env` 文件中可配置以下變數：

- `DB_PATH`：資料庫檔案路徑，預設為 `messages.db`
- `PORT`：伺服器端口，預設為 `8000`

範例 `.env`：
```text
DB_PATH=messages.db
PORT=8000
```

## 貢獻

歡迎提交 Issue 或 Pull Request！請先閱讀 [CONTRIBUTING.md](CONTRIBUTING.md)（可自行創建）。

## 許可證

本專案採用 MIT 許可證，詳見 [LICENSE](LICENSE) 文件。

## 聯繫

有任何問題，請透過 GitHub Issue 聯繫！