# app/schemas/contact_schema.py
from pydantic import BaseModel
from typing import Optional

class ContactBase(BaseModel):
    name: str
    phone: str

class ContactCreate(ContactBase):
    pass

class ContactUpdate(BaseModel):
    
    name: Optional[str] = None
    phone: Optional[str] = None

class ContactResponse(ContactBase):
    
    id: int
    user_id: int  

    model_config = {"from_attributes": True}  
