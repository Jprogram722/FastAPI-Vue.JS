# this file will contain the SQL models and creates tables in the database based on these modesl

from sqlalchemy import Column, Integer, String, Float, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from database import Base

class CategoryModel(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    category_name = Column(String(255))
    __table_args__ = (UniqueConstraint('category_name'),)

    product = relationship('ProductModel', back_populates='category')

class ProductModel(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    category_id = Column(Integer, ForeignKey('category.id'))
    description = Column(String(255), nullable=True)
    price = Column(Float)
    stock = Column(Integer)
    img_path = Column(String(255), nullable=True)

    category = relationship('CategoryModel', back_populates='product')