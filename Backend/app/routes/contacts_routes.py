from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.db.dataBase import get_db
from app.auth.token import get_current_user
from app.schemas.contact_schema import ContactCreate, ContactResponse, ContactBase, ContactUpdate
from app.models.user_model import User
from app.services import contacts_service 

router = APIRouter(tags=["Contacts"])

@router.get("/contacts", response_model=list[ContactBase], status_code=status.HTTP_200_OK)
def get_contacts(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    
    return contacts_service.get_all_contacts(db, current_user.id)



@router.get("/contacts/{name}", response_model=ContactBase, status_code=status.HTTP_200_OK)
def get_contact_by_name(name: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    
    return contacts_service.get_contact_by_name(db, current_user.id, name)



@router.post("/contacts", response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
def create_contact(contact: ContactCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    
    return contacts_service.create_contact(db, current_user.id, contact)



@router.put("/contacts/{name}", response_model=ContactBase, status_code=status.HTTP_200_OK)
def update_contact_by_name(name: str, contact_update: ContactUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    
    return contacts_service.update_contact(db, current_user.id, name, contact_update)



@router.delete("/contacts/{name}", status_code=status.HTTP_200_OK)
def delete_contact_by_name(name: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    
    return contacts_service.delete_contact(db, current_user.id, name)