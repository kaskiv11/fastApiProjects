from typing import Optional, List
import datetime

from pydantic import BaseModel, EmailStr, Field


class Author(BaseModel):
    name: str = Field(..., example="John Sparl", description="Ім'я автора")
    email: EmailStr = Field(..., example="John@gmail.com", description="Електронна пошта")
    bio: Optional[str] = Field(None, example="Коротка біографія автора", description="Біографія автора")


class Article(BaseModel):
    title: str
    content: str
    authors: Author
    tags: Optional[List[str]]
    published_at: Optional[datetime]


class Comment(BaseModel):
    author_name: str
    content: str
    created_at: Optional[datetime] = datetime.now()


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserOut(BaseModel):
    username: str
    email: EmailStr
    is_active: bool = True


class ArticleRequest(BaseModel):
    keywords: List[str]
    date_range: Optional[List[datetime]] = None