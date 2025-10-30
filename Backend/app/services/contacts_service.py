from fastapi import HTTPException, status
from app.models.contact_model import Contact
from sqlalchemy.orm import Session


def get_all_contacts(db, user_id):
    contacts = db.query(Contact).filter(Contact.user_id == user_id).all()
    if not contacts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se encontraron contactos para este usuario."
        )
    return contacts




def get_contact_by_name(db: Session, user_id: int, name: str):

    contact = db.query(Contact).filter(
        Contact.user_id == user_id,
        Contact.name.ilike(f"%{name}%")  
    ).first()

    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contact not found"
        )

    return contact



def create_contact(db: Session, user_id: int, contact_data):

    new_contact = Contact(**contact_data.model_dump(), user_id=user_id)
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return new_contact


def update_contact(db: Session, user_id: int, name: str, contact_update):

    contact = db.query(Contact).filter(
        Contact.user_id == user_id,
        Contact.name.ilike(f"%{name}%")
    ).first()

    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contact not found"
        )

    for key, value in contact_update.model_dump(exclude_unset=True).items():
        setattr(contact, key, value)

    db.commit()
    db.refresh(contact)

    return contact
    

def delete_contact(db: Session, user_id: int, name: str):
    
    contact = db.query(Contact).filter(
        Contact.user_id == user_id,
        Contact.name.ilike(f"%{name}%")
    ).first()

    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contact not found"
        )

    db.delete(contact)
    db.commit()

    return {"message": "Contact deleted successfully"}