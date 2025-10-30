from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session, sessionmaker
from app.db.dataBase import engine
from app.schemas.user_schema import UserCreate, UserResponse
from app.services.auth_service import register_user_service, login_user_service

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(data: UserCreate, db: Session = Depends(get_db)):
    return register_user_service(data, db)


@router.post("/login")
def login_user(data: UserCreate, db: Session = Depends(get_db)):
    return login_user_service(data, db)
