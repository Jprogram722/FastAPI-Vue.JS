# this file will contain the SQL models and creates tables in the database based on these modesl

from sqlalchemy import Column, Integer, String, Float
from database import Base

class ProductModel(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    category = Column(String(255))
    description = Column(String(255), nullable=True)
    price = Column(Float)
    stock = Column(Integer)
    img_path = Column(String(255), nullable=True)