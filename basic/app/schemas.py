from pydantic import BaseModel, Field
from typing import Optional

class ToDoBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    done: bool = False

class ToDoCreate(ToDoBase):
    pass

class ToDoUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    done: Optional[bool] = None

class ToDo(ToDoBase):
    id: int