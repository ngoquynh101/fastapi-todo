# app/models.py
from sqlalchemy import Column, Integer, String, Boolean, Text
from .database import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    name = Column(String(255))
    description = Column(Text)
    completed = Column(Boolean, default=False)
    