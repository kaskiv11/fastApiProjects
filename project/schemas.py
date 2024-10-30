from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import List, Optional


class UserCreate(BaseModel):
    username: str = Field(..., description="Ім'я користувача")
    email: EmailStr = Field(..., description="Електронна пошта")
    password: str = Field(..., description="Пароль")


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True


class ArticleModel(BaseModel):
    title: str = Field(..., description="Назва статті")
    content: str = Field(..., description="Вміст статті")
    author_id: int = Field(..., description="ID автора")


class ArticleResponse(BaseModel):
    id: int
    title: str
    content: str
    author_id: int
    published_at: datetime

    class Config:
        orm_mode = True


class CommentModel(BaseModel):
    author_name: str = Field(..., description="Ім'я автора коментаря")
    content: str = Field(..., description="Текст коментаря")
    article_id: int = Field(..., description="ID статті для коментаря")


class CommentResponse(BaseModel):
    id: int
    author_name: str
    content: str
    created_at: datetime
    article_id: int

    class Config:
        orm_mode = True

