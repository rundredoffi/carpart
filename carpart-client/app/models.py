from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Column, Integer, String
from .database import Base

# ---- SQLAlchemy ORM Model ----
class ClientORM(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)

# ---- Pydantic Schemas ----
class ClientCreate(BaseModel):
    firstname: str
    lastname: str
    email: str

class Client(ClientCreate):
    id: int

    class Config:
        from_attributes = True  # Permet la conversion ORM -> Pydantic

class ClientUpdate(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[str] = None
