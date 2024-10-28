from fastapi import FastAPI, HTTPException, Query
from pydantic import HttpUrl
import httpx
from bs4 import BeautifulSoup

app = FastAPI()


@app.get("/parse/")
async def parse_webpage(url: HttpUrl, element: str = Query("h1")):
    try:
        url_str = str(url)

        async with httpx.AsyncClient() as client:
            response = await client.get(url_str)

        if response.status_code != 200:
            raise HTTPException(status_code=400, detail='Failed to fetch webpage')

        soup = BeautifulSoup(response.text, "html.parser")

        elements = soup.find_all(element)

        if not elements:
            raise HTTPException(status_code=404, detail=f'No {element} tag found')

        parsed_context = [el.get_text(strip=True) for el in elements]

        return {'url': url_str, "element": element, "context": parsed_context}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error parsing: {str(e)}")
