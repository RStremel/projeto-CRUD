from sqlalchemy.orm import Session
from schemas import ProductCreate, ProductUpdate
from models import ProductModel

#get all (select * from)
def get_products(db: Session):
    """
    Função que retorna todos os produtos.
    """
    return db.query(ProductModel).all()

#get product where id = 1
def get_product(db: Session, product_id: int):
    """
    Função que retorna somente um produto usando WHERE.
    """
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()

#insert into (create)
def create_product(db: Session, product: ProductCreate):
    """
    Função que cria um produto na tabela.
    """
    # transformar a instância do Pydant para um modelo do ORM
    db_product = ProductModel(**product.model_dump())
    # add na tabela
    db.add(db_product)
    # commit na tabela
    db.commit()
    # refresh no DB
    db.refresh(db_product)
    # retornar para o usuario o item criado
    return db_product

#delete where id = 1
def delete_product(db: Session, product_id: int):
    """
    Função que deleta somente um produto usando WHERE.
    """
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    db.delete(db_product)
    db.commit()
    return db_product

#update where id = 1    
def update_product(db: Session, product_id: int, product: ProductUpdate):
    """
    Função que faz update de somente um produto usando WHERE.
    """
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if db_product is None:
        return None  
    if product.name is not None:
        db_product.name = product.name
    if product.description is not None:
        db_product.description = product.description
    if product.price is not None:
        db_product.price = product.price
    if product.category is not None:
        db_product.category = product.category
    if product.supplier_email is not None:
        db_product.supplier_email = product.supplier_email

    db.commit()
    db.refresh(db_product)
    return db_product