from fastapi import FastAPI, Request, HTTPException, status, Depends
from pydantic import BaseModel

app = FastAPI()

user_db = {
    "user1": {"username": "user1", "password": "user"},
    "user2": {"username": "admin", "password": "admin"}
}


class User(BaseModel):
    username: str
    role: str


async def auth_middleware(request: Request, call_next):
    token = request.headers.get("Authorization")
    user = user_db.get(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")


async def get_current_user(request: Request) -> User:
    token = request.headers.get("Authorization")
    return user_db.get[token]


@app.get("/admin")
async def admin_route(user: User = Depends(get_current_user)):
    if user.role != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access forbidden")
    return {"message": f"Welcome, admin!"}


@app.get("/user")
async def admin_route(user: User = Depends(get_current_user)):
    return {"message": f"Welcome, {user.username}!"}