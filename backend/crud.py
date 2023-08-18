# this file contains all the controller function for the api

import sqlalchemy.exc
from sqlalchemy.orm import Session
import models, shemas
from helper import get_img_path
import os

def get_products(db: Session, skip: int = 0, limit: int = 100) -> list[dict[any, any]]:
    """
    This function will retreive the all of the products and the details about each product
    and return them to the as a list of dictionaries
    """
    data_db = db.query(
        models.ProductModel.id,
        models.ProductModel.name,
        models.CategoryModel.category_name,
        models.ProductModel.price,
        models.ProductModel.stock,
        models.ProductModel.img_path
    ).join(models.CategoryModel, models.ProductModel.category_id == models.CategoryModel.id).all()

    res = [dict(data._mapping) for data in data_db]

    test = db.query(models.CategoryModel).all()
    print(len(test))
    for i, category in enumerate(test):
        print(i, category.category_name)
    
    return res

def create_product_item(db: Session, item: shemas.ProductSchema) -> models.ProductModel:
    img_path = get_img_path(item.img_file)

    for i, category in enumerate(db.query(models.CategoryModel).all()):
        if (category.category_name == item.category):
            db_category = db.query(models.CategoryModel).filter(models.CategoryModel.id == category.id).first()
        elif (i == len(db.query(models.CategoryModel).all())):
            db_category = models.CategoryModel(
                category_name = item.category
            )

    db_product = models.ProductModel(
        name = item.name,
        category = db_category,
        description = item.description,
        price = item.price,
        stock = item.stock,
        img_path = img_path
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_one_product(db: Session, product_id: int, product: shemas.UpdateProductSchema) -> models.ProductModel:
    staged_product = db.query(models.ProductModel).filter(models.ProductModel.id == product_id).first()
    if staged_product is not None:
        if product.name != None:
            staged_product.name = product.name
        if product.category != None:
            staged_product.category = product.category
        if product.description != None:
            staged_product.description = product.description
        if product.price != None:
            staged_product.price = product.price
        if product.stock != None:
            staged_product.stock = product.stock
        db.commit()
    return staged_product

def delete_one_product(db:Session, product_id: int) -> models.ProductModel:
    staged_product = db.query(models.ProductModel).filter(models.ProductModel.id == product_id).first()
    if staged_product is not None:
        db.delete(staged_product)
        db.commit()
    return staged_product