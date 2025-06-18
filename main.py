from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from datetime import datetime
import sqlite3
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()
DB_PATH = os.getenv("DB_PATH", "messages.db")  # 預設資料庫路徑

# 初始化 FastAPI 應用
app = FastAPI(title="留言系統 API")

# 設置 CORS，允許跨域請求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允許所有來源，實際部署時應限制特定域名
    allow_credentials=True,
    allow_methods=["*"],  # 允許所有 HTTP 方法
    allow_headers=["*"],  # 允許所有標頭
)

# Pydantic 模型：定義留言的輸入格式
class MessageCreate(BaseModel):
    author: str  # 留言作者
    content: str  # 留言內容

# Pydantic 模型：定義留言的完整格式（包含 ID 和創建時間）
class Message(BaseModel):
    id: int  # 留言 ID
    author: str  # 留言作者
    content: str  # 留言內容
    created_at: datetime  # 留言創建時間

# 初始化資料庫
def init_db():
    """創建資料庫和 messages 表格（如果不存在）"""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                author TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

# 啟動時初始化資料庫
init_db()

# 資料庫連線依賴項
def get_db():
    """提供資料庫連線，確保使用後關閉"""
    conn = sqlite3.connect(DB_PATH)
    try:
        yield conn
    finally:
        conn.close()

# API 端點：創建新留言
@app.post("/messages/", response_model=Message)
async def create_message(message: MessageCreate, db: sqlite3.Connection = Depends(get_db)):
    """創建一則新留言並存入資料庫"""
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO messages (author, content) VALUES (?, ?)",
        (message.author, message.content)
    )
    db.commit()
    
    # 獲取剛插入的留言 ID
    message_id = cursor.lastrowid
    cursor.execute("SELECT * FROM messages WHERE id = ?", (message_id,))
    row = cursor.fetchone()
    
    # 回傳完整留言資料
    return Message(
        id=row[0],
        author=row[1],
        content=row[2],
        created_at=row[3]
    )

# API 端點：獲取所有留言
@app.get("/messages/", response_model=List[Message])
async def get_messages(db: sqlite3.Connection = Depends(get_db)):
    """獲取所有留言，按創建時間降序排列"""
    cursor = db.cursor()
    cursor.execute("SELECT * FROM messages ORDER BY created_at DESC")
    rows = cursor.fetchall()
    
    # 將資料庫結果轉為 Message 物件列表
    return [
        Message(id=row[0], author=row[1], content=row[2], created_at=row[3])
        for row in rows
    ]

# API 端點：獲取單一留言
@app.get("/messages/{message_id}", response_model=Message)
async def get_message(message_id: int, db: sqlite3.Connection = Depends(get_db)):
    """根據 ID 獲取指定留言"""
    cursor = db.cursor()
    cursor.execute("SELECT * FROM messages WHERE id = ?", (message_id,))
    row = cursor.fetchone()
    
    # 如果留言不存在，拋出 404 錯誤
    if row is None:
        raise HTTPException(status_code=404, detail="留言不存在")
    
    return Message(id=row[0], author=row[1], content=row[2], created_at=row[3])

# API 端點：更新留言
@app.put("/messages/{message_id}", response_model=Message)
async def update_message(message_id: int, message: MessageCreate, db: sqlite3.Connection = Depends(get_db)):
    """根據 ID 更新指定留言的作者和內容"""
    cursor = db.cursor()
    cursor.execute(
        "UPDATE messages SET author = ?, content = ? WHERE id = ?",
        (message.author, message.content, message_id)
    )
    db.commit()
    
    # 如果沒有更新任何記錄，拋出 404 錯誤
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="留言不存在")
    
    # 回傳更新後的留言
    cursor.execute("SELECT * FROM messages WHERE id = ?", (message_id,))
    row = cursor.fetchone()
    
    return Message(id=row[0], author=row[1], content=row[2], created_at=row[3])

# API 端點：刪除留言
@app.delete("/messages/{message_id}")
async def delete_message(message_id: int, db: sqlite3.Connection = Depends(get_db)):
    """根據 ID 刪除指定留言"""
    cursor = db.cursor()
    cursor.execute("DELETE FROM messages WHERE id = ?", (message_id,))
    db.commit()
    
    # 如果沒有刪除任何記錄，拋出 404 錯誤
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="留言不存在")
    
    return {"message": "留言已成功刪除"}

# 啟動伺服器
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))  # 從環境變數獲取端口，預設 8000
    uvicorn.run(app, host="0.0.0.0", port=port)