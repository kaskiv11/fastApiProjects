import pytest
from fastapi import FastAPI, BackgroundTasks, UploadFile
import asyncio

app = FastAPI()


async def log_data(data: str):
    await asyncio.sleep(1)
    print(f"Логування даних: {data}")


async def progress_data(data: str):
    await asyncio.sleep(1)
    return f"Оброблено: {data}"


@app.post("/process-data")
async def process_data_endpoint(background_tasks: BackgroundTasks, data: str):
    background_tasks.add_task(progress_data, data)
    return {"message": "Дані відправлені на обробку"}


@pytest.mark.asyncio
async def test_progress_data():
    result = await progress_data("test")
    assert result == "Оброблено: test"



