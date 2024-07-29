from pydantic import BaseModel, PositiveFloat, EmailStr, validator, Field
from enum import Enum
from datetime import datetime
from typing import Optional

class ProductBase(BaseModel):
    name: str
    description: str
    price: PositiveFloat
    category: str
    supplier_email: EmailStr

class ProductCreate(ProductBase): #recebe as mesmas validações do ProductBase (id e created_at são criados automaticamente)
    pass

class ProductRead(ProductBase): #será a única que irá se comunicar com o sqlalchemy ORM
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class ProductUpdate(ProductBase): #igual ao Base, porém com Optional, porque posso escolher uma ou várias colunas para o update
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[PositiveFloat] = None
    category: Optional[str] = None
    supplier_email: Optional[EmailStr] = None