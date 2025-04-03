# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHAMY_DATABASE_URL = 'sqlite:///./blog.db' 
connect_args = {"check_same_thread": False}

engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args={"check_same_thread": False})

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
