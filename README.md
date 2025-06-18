# 留言系統 API

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/) [![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0+-green.svg)](https://fastapi.tiangolo.com/) [![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg)](https://www.mysql.com/) [![Docker](https://img.shields.io/badge/Docker-Compose-blue.svg)](https://www.docker.com/) [![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.3-purple.svg)](https://getbootstrap.com/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

這是一個完整的留言系統專案，結合 FastAPI（後端 API）、MySQL（資料庫）、Docker（容器化）與 Bootstrap 5（前端界面）。專案實現了留言的 CRUD 功能，適合 Python 初學者學習全端開發，並可輕鬆部署到雲端。

## 功能

- **創建留言**：透過表單或 POST 請求（`/messages/`）新增留言。
- **獲取留言**：查看所有留言（GET `/messages/`）或單一留言（GET `/messages/{id}`）。
- **更新留言**：編輯留言的作者或內容（PUT `/messages/{id}`）。
- **刪除留言**：刪除指定留言（DELETE `/messages/{id}`）。
- **前端界面**：使用 Bootstrap 5 設計的響應式留言板，支援動態操作。

## 技術棧

- **後端**：FastAPI, SQLAlchemy, Pydantic, Jinja2
- **資料庫**：MySQL 8.0
- **前端**：Bootstrap 5, JavaScript (Fetch API)
- **容器化**：Docker, Docker Compose
- **其他**：python-dotenv, uvicorn

## 專案結構

```
├── backend/
│   ├── app/
│   │   ├── main.py       # FastAPI 主程式
│   │   ├── models.py    # SQLAlchemy 模型
│   │   ├── schemas.py   # Pydantic 模型
│   │   ├── database.py  # 資料庫連線
│   │   └── crud.py      # CRUD 操作
│   ├── requirements.txt # 後端依賴
│   └── Dockerfile       # 後端 Docker 配置
├── frontend/
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   └── js/
│   │       └── main.js
│   └── templates/
│       └── index.html   # Bootstrap 5 頁面
├── .env.example         # 環境變數範例
├── .gitignore           # Git 忽略檔案
├── docker-compose.yml   # Docker Compose 配置
├── LICENSE              # MIT 許可證
└── README.md            # 專案說明
```

## 安裝與運行（本地）

1. **克隆專案**：
   ```bash
   git clone https://github.com/BpsEason/fastapi-message-board.git
   cd fastapi-message-board
   ```

2. **安裝 Docker**：
   確保已安裝 [Docker](https://www.docker.com/get-started) 與 [Docker Compose](https://docs.docker.com/compose/install/)。

3. **配置環境變數**：
   複製 `.env.example` 為 `.env`：
   ```bash
   cp .env.example .env
   ```
   確認 `.env` 中的 `DATABASE_URL` 與 `docker-compose.yml` 的 MySQL 配置一致。

4. **啟動應用**：
   ```bash
   docker-compose up --build
   ```

5. **訪問應用**：
   - **前端界面**：開啟瀏覽器，訪問 `http://localhost:8000`
   - **API 文件**：訪問 `http://localhost:8000/docs`

## 測試

後端包含單元測試（需另行實現，參考先前 `tests.py`）。

1. 安裝測試依賴：
   ```bash
   pip install pytest httpx
   ```

2. 運行測試：
   ```bash
   pytest backend/tests.py -v
   ```

## 環境變數

在 `.env` 文件中配置：

- `DATABASE_URL`：MySQL 連線字串（預設：`mysql+mysqlconnector://user:password@mysql:3306/messages`）
- `PORT`：應用端口（預設：`8000`）

範例 `.env`：
```text
DATABASE_URL=mysql+mysqlconnector://user:password@mysql:3306/messages
PORT=8000
```

## 部署到雲端

1. **選擇平台**：推薦 Render、Heroku 或 AWS。
2. **配置 Docker**：確保 `docker-compose.yml` 與雲端環境相容。
3. **設置環境變數**：在雲端平台配置 `DATABASE_URL` 與 `PORT`。
4. **使用外部 MySQL**：雲端部署建議使用托管 MySQL 服務（如 AWS RDS）。

## 貢獻

歡迎提交 Issue 或 Pull Request！請先開 Issue 討論您的想法，並確保程式碼遵循 PEP 8 規範。

## 許可證

本專案採用 [MIT 許可證](LICENSE)。

## 聯繫

有問題或建議，請透過 [GitHub Issues](https://github.com/BpsEason/fastapi-message-board/issues) 聯繫！