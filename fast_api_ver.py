from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

auth2_scheme = OAuth2PasswordBearer(tokenUrl="123445654645675675675")


def get_current_user(token: str = Depends(auth2_scheme)):
    if token != "секетнийтокен":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token is invalid or expired",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return token


@app.get("/users/me")
async def read_user_me(current_user: str = Depends(get_current_user)):
    return {"user": current_user}


@app.post("/token")
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username == "admin" and form_data.password == "secret":
        return {"access_token": "9042342134241234214", "token_type": "bearer"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token is invalid or expired",
        headers={"WWW-Authenticate": "Bearer"}
    )

