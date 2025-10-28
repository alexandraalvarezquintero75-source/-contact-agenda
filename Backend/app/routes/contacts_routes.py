from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.dataBase import get_db
from app.models.contact_model import Contact
from app.schemas.contact_schema import ContactCreate, ContactResponse
from app.auth.token import get_current_user
from app.models.user_model import User

router = APIRouter(tags=["Contacts"])


@router.post("/contacts", response_model=ContactResponse)
def create_contact(
    contact: ContactCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_contact = Contact(**contact.model_dump(), user_id=current_user.id)
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return new_contact


@router.get("/contacts", response_model=list[ContactResponse])
def get_contacts(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Contact).filter(Contact.user_id == current_user.id).all()



@router.delete("/contacts/{contact_id}")
def delete_contact(
    contact_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    contact = db.query(Contact).filter(Contact.id == contact_id, Contact.user_id == current_user.id).first()
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    db.delete(contact)
    db.commit()
    return {"message": "Contact deleted successfully"}
