"""
Solution 01 — FastAPI Task Manager
"""
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, field_validator
from datetime import datetime, timezone

app = FastAPI(title="Task Manager API", version="1.0.0")
_tasks: dict[int, dict] = {}
_counter = 0


class TaskCreate(BaseModel):
    title: str
    description: str = ""
    priority: int = 1

    @field_validator("priority")
    @classmethod
    def priority_valid(cls, v: int) -> int:
        if v not in (1, 2, 3):
            raise ValueError("Priority must be 1 (low), 2 (medium), or 3 (high)")
        return v

    @field_validator("title")
    @classmethod
    def title_not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Title cannot be empty")
        return v.strip()


class TaskResponse(BaseModel):
    id: int; title: str; description: str
    priority: int; done: bool; created_at: str


@app.get("/tasks", response_model=list[TaskResponse])
async def list_tasks(done: bool | None = None):
    tasks = list(_tasks.values())
    if done is not None:
        tasks = [t for t in tasks if t["done"] == done]
    return tasks


@app.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(task: TaskCreate):
    global _counter
    _counter += 1
    entry = {
        "id": _counter, **task.model_dump(),
        "done": False,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    _tasks[_counter] = entry
    return entry


@app.get("/tasks/{task_id}", response_model=TaskResponse)
async def get_task(task_id: int):
    if task_id not in _tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return _tasks[task_id]


@app.patch("/tasks/{task_id}/done", response_model=TaskResponse)
async def mark_done(task_id: int):
    if task_id not in _tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    _tasks[task_id]["done"] = True
    return _tasks[task_id]


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int):
    if task_id not in _tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del _tasks[task_id]


@app.get("/tasks/stats/summary")
async def stats():
    tasks = list(_tasks.values())
    from collections import Counter
    by_priority = Counter(t["priority"] for t in tasks)
    return {
        "total": len(tasks),
        "done": sum(1 for t in tasks if t["done"]),
        "pending": sum(1 for t in tasks if not t["done"]),
        "by_priority": {"low": by_priority[1], "medium": by_priority[2], "high": by_priority[3]},
    }
