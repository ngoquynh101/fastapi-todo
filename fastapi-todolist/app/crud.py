# app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas

def get_todos(db: Session):
    return db.query(models.Todo).all()

def create_todo(db: Session, todo: schemas.TodoCreate):
    new_todo = models.Todo(**todo.dict())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

def update_todo(db: Session, todo_id: int, todo: schemas.TodoUpdate):
    todo_db = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo_db:
        return None
    for key, value in todo.dict(exclude_unset=True).items():
        setattr(todo_db, key, value)
    db.commit()
    db.refresh(todo_db)
    return todo_db

def delete_todo(db: Session, todo_id: int):
    todo_db = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo_db:
        return None
    db.delete(todo_db)
    db.commit()
    return todo_db
