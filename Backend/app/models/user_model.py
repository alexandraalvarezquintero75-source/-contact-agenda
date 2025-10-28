from sqlalchemy import Column, Integer, String
from app.db.dataBase import Base

class User(Base):
    __tablename__ = "users" #Nombre de la tabla en la base de datos

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(200), unique = True, nullable=False)
    password = Column(String(200), nullable=False)