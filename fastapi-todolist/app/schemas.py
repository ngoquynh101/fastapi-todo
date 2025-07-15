# app/schemas.py
from pydantic import BaseModel
from typing import Optional
class TodoBase(BaseModel):
    title: str
    name: str
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    title: Optional[str] = None
    name: Optional[str] = None
    completed: Optional[bool] = None

class TodoResponse(TodoBase):
    id: int

    class Config:
        orm_mode = True
