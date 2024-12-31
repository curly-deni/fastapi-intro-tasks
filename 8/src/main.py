from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator
from typing import List


app = FastAPI()

# Временная база данных
product_list = []
product_id_counter = 1

# BEGIN (write your solution here)
class ProductSpecifications(BaseModel):
    size: str
    color: str
    material: str

    @validator("size")
    def validate_size(cls, value):
        if not value:
            raise ValueError("Size must be provided.")
        return value

    @validator("color")
    def validate_color(cls, value):
        if not value:
            raise ValueError("Color must be provided.")
        return value

    @validator("material")
    def validate_material(cls, value):
        if not value:
            raise ValueError("Material must be provided.")
        return value

class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0, description="Price must be greater than zero.")
    specifications: ProductSpecifications

    @validator("name")
    def validate_name(cls, value):
        if not value.strip():
            raise ValueError("Name cannot be empty.")
        return value

@app.post("/product")
def add_product(product: Product):
    global product_id_counter

    new_product = {
        "id": product_id_counter,
        "name": product.name,
        "price": product.price,
        "specifications": product.specifications.dict(),
    }
    product_list.append(new_product)
    product_id_counter += 1
    return {"product": new_product, "message": "Product added successfully"}

@app.get("/products")
def get_products():
    return {"products": product_list}
# END
