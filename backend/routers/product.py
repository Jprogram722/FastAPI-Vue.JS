# This file will contain the routes for the propduct portion of the api

import sys

sys.path.append("../")

from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
import models, shemas, crud
from database import get_db

router = APIRouter()

@router.get("/")
async def retreve_products(skip:int=0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_products(db)
    return products

@router.post("/create", response_model=shemas.ProductSchema)
def create_product(product: shemas.ProductSchema, db: Session = Depends(get_db)):
    db_item = crud.create_product_item(db, product)
    return db_item