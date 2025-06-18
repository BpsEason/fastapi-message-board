from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "mysql+mysqlconnector://user:password@mysql:3306/messages")

# 創建 SQLAlchemy 引擎
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 創建會話工廠
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 基類模型
Base = declarative_base()

# 依賴項：獲取資料庫會話
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()