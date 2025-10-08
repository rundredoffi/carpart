from fastapi import FastAPI, HTTPException, Depends
from .models import Client, ClientCreate, ClientUpdate, ClientORM
from .crud import create_client, get_client, update_client, delete_client, get_all_clients
from typing import List
from .database import SessionLocal, engine

ClientORM.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "L'API fonctionne correctement"}

@app.post("/clients/", response_model=Client)
def add_client(client: ClientCreate, db=Depends(get_db)):
    return create_client(db, client)

@app.get("/clients", response_model=List[Client])
def list_all_clients(db=Depends(get_db)):
    return get_all_clients(db)

@app.get("/clients/{client_id}", response_model=Client)
def read_client(client_id: int, db=Depends(get_db)):
    client = get_client(db, client_id)
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@app.put("/clients/{client_id}", response_model=Client)
def update_client_route(client_id: int, client_update: ClientUpdate, db=Depends(get_db)):
    update_data = client_update.model_dump(exclude_unset=True)
    client = update_client(db, client_id, update_data)
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@app.delete("/clients/{client_id}")
def delete_client_route(client_id: int, db=Depends(get_db)):
    client = delete_client(db, client_id)
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return {"message": "Client deleted successfully"}