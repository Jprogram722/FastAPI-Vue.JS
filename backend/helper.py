# this file will contain helper functions

import models
from sqlalchemy.orm import Session

def get_img_path(img_file: str) -> str:
    """
    This function will take in a img file as a string and concatinate it will a folder path string

    Example:
    >>> get_img_path("phone.png")
    >>> "\\src\\pics\\phone.png"
    """

    if img_file is not None:
        pic_folder = '\\src\\pics\\'
        img_path = pic_folder + img_file
    else:
        img_path = img_file

    return img_path

def check_uniqueness(category_name: str, db: Session) -> models.CategoryModel:
    """
    This function will take in a category name and a database session to check and see if a category has already been created
    in the SQL database

    Example:
    >>> check_uniqueness("electronics", db)
    >>> <models.CategoryModel at "some memory address">
    """

    for category in db.query(models.CategoryModel).all():
        if (category_name == category.category_name):
            return db.query(models.CategoryModel).filter(models.CategoryModel.id == category.id).first()
    return models.CategoryModel(category_name = category_name)

