from fastapi import FastAPI, APIRouter,Depends, HTTPException, Query
from db import get_db
from typing import List
from schemas.schemas import CreateProduct, UpdateProduct
from models.models import Product
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

router= APIRouter()

@router.get('/')
def home():
    return {"message":"Welcome to ECOMMERCE API"}


@router.post('/create')
def create_product(product:CreateProduct,  db:Session = Depends(get_db)):
    new_user = Product(
        id=product.id,
        name= product.name,
        description = product.description,
        price = product.price,
        stock= product.stock,
        category= product.category
    )
    db.add(new_user)
    db.commit()
    return JSONResponse(status_code= 201, content={"message":"Product created Successfully."})


@router.get('/products')
def get_products(db:Session = Depends(get_db)):
    products = db.query(Product).all()
    if len(products) == 0:
        return []
    
    return products

@router.get('/products/{product_id}')
def get_by_id(product_id:int, db:Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


@router.delete('/products/{product_id}')
def delete_product(product_id:int , db:Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(product)
    db.commit()

    return JSONResponse(status_code= 200 , content={"message":"Product deleted Successfully."})


@router.put('/products/{product_id}')
def update_product(product_id:int,product:UpdateProduct, db:Session= Depends(get_db)):
    existing_product = db.query(Product).filter(Product.id == product_id).first()
    

    if not existing_product:
        raise HTTPException(status_code=404, detail="Product not found")

    updated_product = product.model_dump(exclude_unset=True)

    for k,v in updated_product.items():
        setattr(existing_product,k,v)

    db.commit()
    db.refresh(existing_product)
    
    return JSONResponse( status_code=200, content="Product updated Successfully.")


@router.get('/products/filter/', response_model=List[CreateProduct])
def filter_products(category:str =Query(description="Filter products by category"), price:float = Query(description="Filter products by price"), db:Session = Depends(get_db)):
    category_data= db.query(Product).filter(Product.category == category | Product.price <= price).all()
    # price_data = db.query(Product).filter(Product.price == price).all()
    return category_data




        



