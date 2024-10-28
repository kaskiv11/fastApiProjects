from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

auth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

fake_token_db = {
    "mysecerttoken": {'username': 'user1'},
    "anothersecrettoken": {'username': 'user2'}
}


@app.get("/user/me")
async def read_user_me(token: str = Depends(auth2_scheme)):
    if token not in fake_token_db:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"username": fake_token_db[token]["username"]}