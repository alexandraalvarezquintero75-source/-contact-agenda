from pydantic import BaseModel, EmailStr, Field, field_validator
import re

class UserBase(BaseModel):
    email: EmailStr = Field(..., description="User Email")

class UserCreate(UserBase):
    password: str = Field(..., min_length=8, description="Secure password")

    @field_validator("password")
    def validate_password(cls, password):
        if len(password) < 8:
            raise ValueError("The password must be at least 8 characters long.")
        
        if not re.search(r"[A-Z]", password):
            raise ValueError("The password must include at least one uppercase letter.")
        
        if len(re.findall(r"\d", password)) < 2:
            raise ValueError("The password must contain at least two numbers.")
        
        return password


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True
