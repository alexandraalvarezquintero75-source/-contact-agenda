from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.dataBase import Base

class Contact(Base):
    __tablename__ = "Contacts"

    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(100))
    phone = Column(String(20))
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates = "contacts")