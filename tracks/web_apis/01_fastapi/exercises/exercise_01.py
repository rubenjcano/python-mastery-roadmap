"""
Exercise 01 — FastAPI
=======================
Build a simple Task Manager API.

Run: uvicorn exercise_01:app --reload
Test: visit http://localhost:8000/docs
"""
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, field_validator
from datetime import datetime


app = FastAPI(title="Task Manager API", version="1.0.0")

# In-memory store (no database needed for this exercise)
_tasks: dict[int, dict] = {}
_counter = 0


# ── Models ────────────────────────────────────────────────────────────────

class TaskCreate(BaseModel):
    title: str
    description: str = ""
    priority: int = 1   # 1=low, 2=medium, 3=high

    @field_validator("priority")
    @classmethod
    def priority_valid(cls, v: int) -> int:
        # TODO: validate priority is 1, 2, or 3
        ...
        return v

    @field_validator("title")
    @classmethod
    def title_not_empty(cls, v: str) -> str:
        # TODO: validate title is not blank
        ...
        return v


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    priority: int
    done: bool
    created_at: str


# ── Endpoints ─────────────────────────────────────────────────────────────

@app.get("/tasks", response_model=list[TaskResponse])
async def list_tasks(done: bool | None = None):
    """Return all tasks. Optional filter: ?done=true or ?done=false"""
    # TODO: return tasks, filtering by done status if provided
    ...


@app.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(task: TaskCreate):
    """Create a new task."""
    # TODO: add task to _tasks, return it with id and created_at
    ...


@app.get("/tasks/{task_id}", response_model=TaskResponse)
async def get_task(task_id: int):
    """Get a single task. Return 404 if not found."""
    # TODO
    ...


@app.patch("/tasks/{task_id}/done", response_model=TaskResponse)
async def mark_done(task_id: int):
    """Mark a task as done."""
    # TODO
    ...


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int):
    """Delete a task."""
    # TODO
    ...


@app.get("/tasks/stats/summary")
async def stats():
    """Return: total, done, pending, by_priority counts."""
    # TODO
    ...
