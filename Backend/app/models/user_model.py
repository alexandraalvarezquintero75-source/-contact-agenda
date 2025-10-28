from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.dataBase import Base

class User(Base):
    __tablename__ = "users" 

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(200), unique = True, nullable=False)
    password = Column(String(200), nullable=False)

    contacts = relationship("Contact", back_populates="owner")