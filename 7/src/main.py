from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List


app = FastAPI()

# Временная база данных
product_list = []
product_id_counter = 1

# BEGIN (write your solution here)
class Product(BaseModel):
    name: str = Field(..., title="Название продукта", min_length=1)
    price: float = Field(..., gt=0, title="Цена продукта")
    quantity: int = Field(..., ge=0, title="Количество на складе")

@app.post("/product")
def add_product(product: Product):
    global product_id_counter

    new_product = product.dict()

    new_product["id"] = product_id_counter
    product_list.append(new_product)

    product_id_counter += 1

    return {"product": new_product, "message": "Product added successfully"}

@app.get("/products")
def get_products():
    if not product_list:
        raise HTTPException(status_code=404, detail="No products found")
    return {"products": product_list}
# END
