from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import init_db, get_db
from crud import create_user, get_user, create_article, get_articles, get_article, create_comment, get_comments
from schemas import UserCreate, UserResponse, ArticleModel, ArticleResponse, CommentModel, CommentResponse
from auth import authenticate_user

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.on_event("startup")
def startup_event():
    init_db()


@app.post("/register/", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    user.hashed_password = authenticate_user(db, user.hashed_password)
    return create_user(db)


@app.get("users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db())):
    return get_user(db, user_id)


@app.post("/articles/", response_model=ArticleResponse)
def create_article(article: ArticleModel, db: Session = Depends(get_db)):
    return create_article(db=db, article=article)
