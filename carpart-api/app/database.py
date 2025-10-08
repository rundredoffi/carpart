from motor.motor_asyncio import AsyncIOMotorClient
import os

# Configuration MongoDB depuis les variables d'environnement
MONGO_HOST = os.getenv("MONGO_HOST", "carpart-mongo")
MONGO_PORT = os.getenv("MONGO_PORT", "27017")
MONGO_DATABASE = os.getenv("MONGO_DATABASE", "carpart")

# Construction de l'URL de connexion
MONGO_DETAILS = f"mongodb://{MONGO_HOST}:{MONGO_PORT}"

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client[MONGO_DATABASE]
product_collection = database.get_collection("products")
