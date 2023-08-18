# this file contains all the controller function for the api

from sqlalchemy.orm import Session
import models, shemas
import os

def get_products(db: Session, skip: int = 0, limit: int = 100):
    data_db = db.query(
        models.ProductModel.id,
        models.ProductModel.name,
        models.CategoryModel.category_name,
        models.ProductModel.price,
        models.ProductModel.stock,
        models.ProductModel.img_path
    ).join(models.CategoryModel, models.ProductModel.category_id == models.CategoryModel.id).all()

    res = [dict(data._mapping) for data in data_db]

    #test = [dict(data._mapping) for data in db.query(models.CategoryModel.category_name).all()]
    #for category in test:
    #    print(category['category_name'])
    
    return res

def create_product_item(db: Session, item: shemas.ProductSchema) -> models.ProductModel:
    if item.img_file is not None:
        pic_folder = '\\src\\pics\\'
        img_path = pic_folder + item.img_file
    else:
        img_path = item.img_file

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

def update_one_product(db: Session, product_id: int, product: shemas.UpdateProductSchema):
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

def delete_one_product(db:Session, product_id: int) -> bool:
    staged_product = db.query(models.ProductModel).filter(models.ProductModel.id == product_id).first()
    if staged_product is not None:
        db.delete(staged_product)
        db.commit()
    return staged_product