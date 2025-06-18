from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.requests import Request
from sqlalchemy.orm import Session
from . import models, schemas, crud, database
from typing import List
import os

# 初始化 FastAPI 應用
app = FastAPI(title="留言系統 API")

# 創建資料庫表格
models.Base.metadata.create_all(bind=database.engine)

# 掛載靜態檔案與模板
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend/templates")

# API 端點：獲取首頁
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """渲染前端首頁"""
    return templates.TemplateResponse("index.html", {"request": request})

# API 端點：創建留言
@app.post("/messages/", response_model=schemas.Message)
async def create_message(message: schemas.MessageCreate, db: Session = Depends(database.get_db)):
    """創建新留言並存入 MySQL"""
    return crud.create_message(db=db, message=message)

# API 端點：獲取所有留言
@app.get("/messages/", response_model=List[schemas.Message])
async def get_messages(db: Session = Depends(database.get_db)):
    """獲取所有留言，按創建時間降序排列"""
    return crud.get_messages(db=db)

# API 端點：獲取單一留言
@app.get("/messages/{message_id}", response_model=schemas.Message)
async def get_message(message_id: int, db: Session = Depends(database.get_db)):
    """根據 ID 獲取指定留言"""
    db_message = crud.get_message(db=db, message_id=message_id)
    if db_message is None:
        raise HTTPException(status_code=404, detail="留言不存在")
    return db_message

# API 端點：更新留言
@app.put("/messages/{message_id}", response_model=schemas.Message)
async def update_message(message_id: int, message: schemas.MessageCreate, db: Session = Depends(database.get_db)):
    """根據 ID 更新留言"""
    db_message = crud.update_message(db=db, message_id=message_id, message=message)
    if db_message is None:
        raise HTTPException(status_code=404, detail="留言不存在")
    return db_message

# API 端點：刪除留言
@app.delete("/messages/{message_id}")
async def delete_message(message_id: int, db: Session = Depends(database.get_db)):
    """根據 ID 刪除留言"""
    if not crud.delete_message(db=db, message_id=message_id):
        raise HTTPException(status_code=404, detail="留言不存在")
    return {"message": "留言已成功刪除"}