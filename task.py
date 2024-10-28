from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI()


class Task(BaseModel):
    title: str = Field(..., examples="Buy products")
    description:  Optional[str] = Field(None, examples="Get milk, bread")
    is_completed: bool = Field(False, examples=False)

tasks = []
task_id_counter = 1


@app.post("/tasks", response_model=dict)
def create_task(task: Task):
    global task_id_counter
    task_dict = task.dict()
    task_dict['id'] = task_id_counter
    tasks.append(task_dict)
    task_id_counter += 1
    return {"message":"Task created successfully", "task": task_dict}


@app.get("/task", response_model=List[Task])
def get_all_tasks():
    return tasks


@app.delete("/task/{task_id}", response_model=dict)
def delete_task(task_id: str):
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
        return {'message': 'Task deleted successfully'}
    raise HTTPException(status_code=404, detail="Task not found")


def get_items_from_database(skip: int, limit: int ):
    items = get_items_from_database(skip, limit)
    return {'items': items}


@app.get("/items/")
async def read_items(skip: int = Query(0, title='Пропустити', description="Скільки записів пропустити"),
                     limit: int = Query(10, title="Limit", description="Максимальна кількість запитів на вихід")):
    all_items = [{"item_id": i, "name": f"Item{i}"} for i in range(1, 101)]
    return all_items[skip:skip+limit]





