# this file will contain the schemas for the info of a product using pydantic

from pydantic import BaseModel

class ProductSchema(BaseModel):
    id: int | None = None
    name: str
    category: str
    description: str | None = None
    price: float
    stock: int
    img_file: str | None = None

    class Config:
        from_attributes = True

class UpdateProductSchema(BaseModel):
    id: int
    name: str | None = None
    category: str | None = None
    description: str | None = None
    price: float | None = None
    stock: int | None = None
    img_file: str | None = None

    class Config:
        from_attributes = True