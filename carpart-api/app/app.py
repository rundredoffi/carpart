from fastapi import FastAPI, HTTPException
from app.models import Product, ProductCreate, ProductUpdate
from app.crud import create_product, get_product, update_product, delete_product, get_all_products
from typing import List

app = FastAPI()
"""
Route principal
"""
@app.get("/")
async def root():
    return {"message":"L'API fonctionne correctement"}
"""
Route pour créer un produit
"""
@app.post("/products/", response_model=Product)
async def add_product(product: ProductCreate):
    return await create_product(product)
"""
Route pour récupérer tous les produits de la base
"""
@app.get("/products", response_model=List[Product])
async def list_all_products():
    return await get_all_products()
"""
Route pour récupérer les détails d'un produit
"""
@app.get("/products/{product_id}", response_model=Product)
async def read_product(product_id: str):
    product = await get_product(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
"""
Route pour mettre à jour un produit avec son _id
"""
@app.put("/products/{product_id}", response_model=Product)
async def modify_product(product_id: str, product_update: ProductUpdate):
    product = await update_product(product_id, **product_update.dict(exclude_unset=True))
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
"""
Route pour supprimer un produit avec son _id
"""
@app.delete("/products/{product_id}")
async def remove_product(product_id: str):
    return await delete_product(product_id)
