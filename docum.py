from fastapi import FastAPI, Query, Path
from typing import List, Optional

app = FastAPI()


@app.get('/items/', summary="Пошук елементів")
async def search_items(
        q: Optional[str] = Query(None,
                                 title="Пошукові запити",
                                 description="Список пошукових запитів",
                                 alias="query",
                                 min_length=3,
                                 max_length=50,
                                 deprecated=True),
        item_id: int = Path(..., title="ID елемента", description="Унікальний номер", gt=0)):
    return {"q": q, 'item_id': item_id}
