from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI()

# Модель даних для завдання
class Task(BaseModel):
    title: str = Field(..., example="Buy groceries")
    description: Optional[str] = Field(None, example="Get milk and bread")
    is_completed: bool = Field(False, example=False)

# Список для зберігання завдань
tasks = []
task_id_counter = 1

# Додавання нового завдання
@app.post("/tasks/", response_model=dict)
def create_task(task: Task):
    global task_id_counter
    task_dict = task.dict()
    task_dict["id"] = task_id_counter
    tasks.append(task_dict)
    task_id_counter += 1
    return {"message": "Task created successfully", "task": task_dict}


# Отримання списку всіх завдань
@app.get("/tasks/", response_model=List[Task])
def get_all_tasks():
    return tasks

# Видалення завдання
@app.delete("/tasks/{task_id}", response_model=dict)
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")
