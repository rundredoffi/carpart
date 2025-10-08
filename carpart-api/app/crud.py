from bson import ObjectId
from app.models import ProductCreate
from app.database import product_collection

# Conversion du _id en id pour FastAPI
def serialize_product(product: dict) -> dict:
    if not product:
        return None
    product["id"] = str(product["_id"])
    product.pop("_id", None)  # Supprime _id pour éviter les conflits
    return product

async def create_product(product: ProductCreate):
    product_dict = product.model_dump()
    result = await product_collection.insert_one(product_dict)
    product_dict["id"] = str(result.inserted_id)
    return product_dict

async def get_product(product_id: str):
    product = await product_collection.find_one({"_id": ObjectId(product_id)})
    return serialize_product(product)

async def get_all_products():
    # Récupère tous les produits avec find()
    cursor = product_collection.find()
    products = await cursor.to_list(length=None)  # length=None récupère tous les documents

    # Sérialise chaque produit pour convertir _id -> id
    return [serialize_product(p) for p in products]

async def update_product(product_id: str, **kwargs):
    update_data = {k: v for k, v in kwargs.items() if v is not None}
    if not update_data:
        product = await product_collection.find_one({"_id": ObjectId(product_id)})
        return serialize_product(product)

    await product_collection.update_one(
        {"_id": ObjectId(product_id)},
        {"$set": update_data}
    )
    product = await product_collection.find_one({"_id": ObjectId(product_id)})
    return serialize_product(product)

async def delete_product(product_id: str):
    await product_collection.delete_one({"_id": ObjectId(product_id)})
    return {"message": "Product deleted successfully"}