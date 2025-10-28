# app/schemas/contact_schema.py
from pydantic import BaseModel
from typing import Optional

class ContactBase(BaseModel):
    name: str
    phone: str
    email: Optional[str] = None

class ContactCreate(ContactBase):
    """Modelo que el cliente envía al crear un contacto."""
    pass

class ContactUpdate(BaseModel):
    """Modelo para actualizar (campos opcionales)."""
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None

class ContactResponse(ContactBase):
    """Modelo que devolvemos al cliente (incluye id)."""
    id: int
    user_id: int  # id del dueño/usuario; úsalo para filtrar y comprobar permisos

    model_config = {"from_attributes": True}  # para Pydantic v2
