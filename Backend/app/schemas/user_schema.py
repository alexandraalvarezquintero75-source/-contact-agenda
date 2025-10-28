from pydantic import BaseModel, EmailStr, field_validator
from fastapi import HTTPException
import re

class UserBase(BaseModel):
    email: EmailStr = field_validator(..., description="Correo del Usuario")

class UserCreate(UserBase):
    password: str = field_validator(...,min_length=8, description="Contraseña segura")

    @field_validator("password")
    def validate_password(cls, values):

        password= (values.get("password"))

        if len(password) <8:
            raise HTTPException(
                status_code=422,
                detail="La contraseña debe tener al menos 8 caracteres."
            )
        
        if not re.search(r"[A-Z", password):
            raise HTTPException(
                status_code=422,
                detail="La contraseña debe incluir al menos una letra mayúscula."
            )
        
        if len(re.findall(r"/d", password)) <2:
            raise HTTPException(
                status_code=422,
                detail="La contraseña debe contener al menos dos números."
            )
        
        return values
    
class UserResponsable(BaseModel):
    ind: int
    email: EmailStr

    class Confing:
        orm_mode = True