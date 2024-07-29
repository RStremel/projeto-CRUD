from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base

#importa do Base para dizer que vai funcionar como um ORM
class ProductModel(Base):
    __tablename__ = "products" #vai ser o nome da minha tabela

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    category = Column(String)
    supplier_email = Column(String)
    created_at = Column(DateTime(timezone=True), default=func.now())