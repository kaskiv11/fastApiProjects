from fastapi import FastAPI, Query, Path
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from sqlalchemy.orm import Session
import crud, models, schemas


auth2_scheme = OAuth2PasswordBearer(tokenUrl="url")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str):
    return pwd_context.hash(password)


def authenticate_user(db: Session, username: str, password: str):
    user = crud.get_user_by_username(db, username)

    if user and verify_password(password, user.has_password):
        return user
    return False