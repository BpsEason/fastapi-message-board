# 留言系統 API

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/) [![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0+-green.svg)](https://fastapi.tiangolo.com/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

這是一個使用 Python 和 FastAPI 開發的簡單留言系統 RESTful API，適合 Python 初學者學習 Web 後端開發。專案使用 SQLite 儲存留言資料，支援完整的 CRUD（創建、讀取、更新、刪除）功能，並包含單元測試與環境變數配置。

## 功能

- **創建留言**：發送 POST 請求到 `/messages/`，新增留言（包含作者與內容）。
- **獲取所有留言**：發送 GET 請求到 `/messages/`，查看所有留言（按創建時間降序排列）。
- **獲取單一留言**：發送 GET 請求到 `/messages/{id}`，查詢指定留言。
- **更新留言**：發送 PUT 請求到 `/messages/{id}`，修改留言的作者或內容。
- **刪除留言**：發送 DELETE 請求到 `/messages/{id}`，刪除指定留言。

## 技術棧

- **Python 3.8+**：程式語言
- **FastAPI**：高效的 Web 框架，支援異步處理
- **SQLite**：輕量級資料庫，無需額外伺服器
- **Pydantic**：數據驗證與型別檢查
- **python-dotenv**：環境變數管理
- **pytest & httpx**：用於單元測試

## 專案結構

```
├── main.py           # 主應用程式，包含 API 端點與資料庫邏輯
├── tests.py         # 單元測試程式碼
├── requirements.txt # 依賴清單
├── .env.example     # 環境變數範例
├── .gitignore       # Git 忽略檔案清單
├── LICENSE          # MIT 許可證
└── README.md        # 專案說明文件
```

## 安裝與運行

1. **克隆專案**：
   ```bash
   git clone https://github.com/BpsEason/fastapi-message-board.git
   cd fastapi-message-board
   ```

2. **創建虛擬環境（推薦）**：
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
   可根據需要修改 `.env` 中的 `DB_PATH`（資料庫路徑）或 `PORT`（伺服器端口）。

5. **運行應用**：
   ```bash
   python main.py
   ```

6. **訪問 API 文件**：
   開啟瀏覽器，訪問 `http://localhost:8000/docs`，使用 Swagger UI 測試 API 端點。

## 測試

專案包含單元測試，使用 `pytest` 和 `httpx` 驗證 API 功能。

1. 安裝測試依賴：
   ```bash
   pip install pytest httpx
   ```

2. 運行測試：
   ```bash
   pytest tests.py -v
   ```

## 環境變數

在 `.env` 文件中可配置以下變數：

- `DB_PATH`：資料庫檔案路徑（預設：`messages.db`）
- `PORT`：伺服器端口（預設：`8000`）

範例 `.env`：
```text
DB_PATH=messages.db
PORT=8000
```

## 部署指引

您可以將此 API 部署到雲端平台（如 Render、Heroku 或 Vercel）。以下是基本步驟：

1. 確保 `requirements.txt` 包含所有依賴。
2. 在部署平台上設置環境變數（`DB_PATH` 和 `PORT`）。
3. 使用 `uvicorn` 啟動應用：
   ```bash
   uvicorn main:app --host 0.0.0.0 --port $PORT
   ```

**注意**：SQLite 適合本地開發，生產環境建議使用 PostgreSQL 或 MySQL，並相應修改資料庫連線邏輯。

## 貢獻

歡迎提交 Issue 或 Pull Request！若想貢獻程式碼，請先開 Issue 討論您的想法。提交前請確保程式碼通過測試並遵循 PEP 8 規範。

## 許可證

本專案採用 [MIT 許可證](LICENSE)，歡迎自由使用與分享。

## 聯繫

有任何問題或建議，請透過 [GitHub Issues](https://github.com/BpsEason/fastapi-message-board/issues) 聯繫！