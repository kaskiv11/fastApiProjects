from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()


@app.middleware("http")
async def authenticate_request(request: Request, call_next):
    token = request.headers.get("Authorization")
    if not token or not validate_token(token):
        return JSONResponse(status_code=401, content={"detail": "Invalid token"})

    response = await call_next(request)
    return response


def validate_token(token: str) -> bool:
    return token


@app.get("/endpoint")
def endpoint():
    return {"message": "Secure Endpoint is working"}