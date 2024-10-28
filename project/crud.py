from sqlalchemy.orm import Session
import models, schemas, auth


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter_by(username == models.User.username).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
