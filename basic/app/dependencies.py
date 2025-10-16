from typing import Dict
from fastapi import Depends
from .config import settings

class ToDoService:
    def __init__(self) -> None:
        self._store: Dict[int, Dict] = {}
        self._counter = 0

    def list(self):
        return list(self._store.values())
    
    def get(self, todo_id:int):
        return self._store.get(todo_id)
    
    def create(self, title: str, done: bool = False):
        self._counter += 1
        todo = {"id": self._counter, "title": title, "done": done}
        self._store[self._counter] = todo
        return todo
    
    def update(self, todo_id: int, *, title = None, done = None):
        todo = self._store.get(todo_id)
        if not todo:
            return None
        if title is not None:
            todo["title"] = title
        if done is not None:
            todo["done"] = done
        return todo
    
    def delete(self, todo_id:int) -> bool:
        return self._store.pop(todo_id, None) is not None
    

def get_settings():
    return settings

_service = ToDoService()

def get_todo_service() -> ToDoService:
    return _service