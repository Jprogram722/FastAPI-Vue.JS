"""
Routes related to the categories table for the api
"""

import sys

sys.path.append("../")

from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
import models, shemas
from database import get_db

router = APIRouter()

@router.get("/")
def get_categories(db: Session = Depends(get_db)):
    return db.query(models.CategoryModel).all()

@router.post("/create", response_model=shemas.CategorySchema)
def create_category(item: shemas.CategorySchema, db: Session = Depends(get_db)):
    new_category = models.CategoryModel(
        category = item.category
    )

    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category


