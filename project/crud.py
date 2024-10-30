from sqlalchemy.orm import Session
from models import User, Article, Comment
from schemas import UserCreate, ArticleModel, CommentModel


def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username, email=user.email, hashed_password=user.password)  # Хешування пароля реалізується в auth.py
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def create_article(db: Session, article: ArticleModel):
    db_article = Article(**article.dict())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article


def get_articles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Article).offset(skip).limit(limit).all()


def get_article(db: Session, article_id: int):
    return db.query(Article).filter(Article.id == article_id).first()


def update_article(db: Session, article_id: int, article: ArticleModel):
    db_article = db.query(Article).filter(Article.id == article_id).first()
    if db_article:
        for key, value in article.dict().items():
            setattr(db_article, key, value)
        db.commit()
        db.refresh(db_article)
        return db_article
    return None


def delete_article(db: Session, article_id: int):
    db_article = db.query(Article).filter(Article.id == article_id).first()
    if db_article:
        db.delete(db_article)
        db.commit()
        return db_article
    return None


def create_comment(db: Session, comment: CommentModel):
    db_comment = Comment(**comment.dict())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def get_comments(db: Session, article_id: int):
    return db.query(Comment).filter(Comment.article_id == article_id).all()


def update_comment(db: Session, comment_id: int, comment: CommentModel):
    db_comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if db_comment:
        for key, value in comment.dict().items():
            setattr(db_comment, key, value)
        db.commit()
        db.refresh(db_comment)
        return db_comment
    return None


def delete_comment(db: Session, comment_id: int):
    db_comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if db_comment:
        db.delete(db_comment)
        db.commit()
        return db_comment
    return None

