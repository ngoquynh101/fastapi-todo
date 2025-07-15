# app/schemas.py
from pydantic import BaseModel
from typing import Optional
class TodoBase(BaseModel):
    title: str
    completed: bool = False

class TodoCreate(TodoBase):
    title: str
    description: Optional[str] = None

class TodoUpdate(TodoBase):
    title: Optional[str] = None
    completed: Optional[bool] = None

class TodoResponse(TodoBase):
    id: int

    class Config:
        orm_mode = True
