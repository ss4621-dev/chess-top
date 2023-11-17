# app/db/database.py

from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database

DATABASE_URL = "postgresql://shekhar:121004@localhost/chess_database"

database = Database(DATABASE_URL)
metadata = create_engine(DATABASE_URL)

Base = declarative_base()

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    rating_history = Column(JSON)

Base.metadata.create_all(bind=metadata)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=metadata)
