from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session, sessionmaker
from app.db.dataBase import engine
from app.models.user_model import User
from app.schemas.user_schema import UserCreate, UserResponse
from app.auth.token import create_access_token
from sqlalchemy import select
import bcrypt

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
    existing_user = db.execute(select(User).where(User.email == data.email)).scalar_one_or_none()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El correo electrónico ya está registrado"
        )

    hashed_password = bcrypt.hashpw(data.password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    new_user = User(email=data.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user



@router.post("/login")
def login_user(data: UserCreate, db: Session = Depends(get_db)):
    user = db.execute(select(User).where(User.email == data.email)).scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El correo no está registrado"
        )


    if not bcrypt.checkpw(data.password.encode("utf-8"), user.password.encode("utf-8")):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Contraseña incorrecta"
        )

    
    access_token = create_access_token(data={"sub": str(user.id)})

    return {
        "message": "Inicio de sesión exitoso",
        "access_token": access_token,
        "token_type": "bearer"
    }
