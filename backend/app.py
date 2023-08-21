"""
Author: Jared Park
This will be the backend to the ecommerce website using fastapi and SQL for the backend
See Docs for FastAPI on how to use it
"""

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from shemas import ProductSchema, UpdateProductSchema
import models
import crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

# depedency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI(
    title="Product API",
    description="a REST API using python and mysql to store information about products",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/api/')
async def retreve_products(skip:int=0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_products(db)
    return products

@app.get('/api/get_one/{product_id}')
async def retreve_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_one_product(db, product_id)
    return product

@app.post('/api/form')
async def create_product(product: ProductSchema, db: Session = Depends(get_db)):
    db_item = crud.create_product_item(db, product)
    return db_item

@app.patch('/api/update/{product_id}')
def update_product(product_id: int, product: UpdateProductSchema , db: Session = Depends(get_db)):
    updated_product = crud.update_one_product(db, product_id, product)
    if updated_product is None:
        raise HTTPException(status_code = 404, detail=f"No Product With ID Of {product_id}")
    return updated_product

@app.delete("/api/delete/{product_id}")
async def delete_product(product_id: int, db: Session = Depends(get_db)):
    del_product = crud.delete_one_product(db, product_id)
    if del_product is None:
        raise HTTPException(status_code = 404, detail=f"No Product With ID Of {product_id}")
    return del_product


