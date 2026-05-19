# FastAPI

## Minimal app
```python
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel

app = FastAPI(title="My API", version="1.0.0")

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

items: dict[int, Item] = {}

@app.get("/items/{item_id}")
async def get_item(item_id: int) -> Item:
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@app.post("/items", status_code=status.HTTP_201_CREATED)
async def create_item(item: Item) -> dict:
    item_id = len(items) + 1
    items[item_id] = item
    return {"id": item_id, **item.model_dump()}
```

## Dependency injection
```python
from fastapi import Depends
from functools import lru_cache

class Settings(BaseModel):
    db_url: str = "sqlite:///./test.db"
    secret_key: str = "changeme"

@lru_cache
def get_settings() -> Settings:
    return Settings()

@app.get("/config")
async def show_config(settings: Settings = Depends(get_settings)):
    return {"db": settings.db_url}
```

## Background tasks
```python
from fastapi import BackgroundTasks

def send_email(email: str, message: str) -> None:
    # slow operation — runs after response is sent
    print(f"Sending to {email}: {message}")

@app.post("/notify")
async def notify(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, email, "Your job is done!")
    return {"status": "queued"}
```

## Run
```bash
uvicorn main:app --reload --port 8000
# Docs at: http://localhost:8000/docs
```
