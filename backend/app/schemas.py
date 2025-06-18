from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# 創建留言的輸入格式
class MessageCreate(BaseModel):
    author: str
    content: str

# 完整留言的輸出格式
class Message(BaseModel):
    id: int
    author: str
    content: str
    created_at: datetime

    class Config:
        orm_mode = True  # 支援 SQLAlchemy ORM 轉換