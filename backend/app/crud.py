from sqlalchemy.orm import Session
from . import models, schemas

# 創建留言
def create_message(db: Session, message: schemas.MessageCreate):
    db_message = models.Message(author=message.author, content=message.content)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

# 獲取所有留言
def get_messages(db: Session):
    return db.query(models.Message).order_by(models.Message.created_at.desc()).all()

# 獲取單一留言
def get_message(db: Session, message_id: int):
    return db.query(models.Message).filter(models.Message.id == message_id).first()

# 更新留言
def update_message(db: Session, message_id: int, message: schemas.MessageCreate):
    db_message = db.query(models.Message).filter(models.Message.id == message_id).first()
    if db_message:
        db_message.author = message.author
        db_message.content = message.content
        db.commit()
        db.refresh(db_message)
    return db_message

# 刪除留言
def delete_message(db: Session, message_id: int):
    db_message = db.query(models.Message).filter(models.Message.id == message_id).first()
    if db_message:
        db.delete(db_message)
        db.commit()
        return True
    return False