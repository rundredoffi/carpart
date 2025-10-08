from .models import ClientORM as Client
from sqlalchemy.orm import Session

def create_client(db: Session, client):
    db_client = Client(
        firstname=client.firstname,
        lastname=client.lastname,
        email=client.email
    )
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_client(db: Session, client_id: int):
    return db.query(Client).filter(Client.id == client_id).first()

def get_all_clients(db: Session):
    return db.query(Client).all()

def update_client(db: Session, client_id: int, update_data):
    db_client = db.query(Client).filter(Client.id == client_id).first()
    if db_client:
        for key, value in update_data.items():
            if value is not None:
                setattr(db_client, key, value)
        db.commit()
        db.refresh(db_client)
    return db_client

def delete_client(db: Session, client_id: int):
    db_client = db.query(Client)
    db_client = db_client.filter(Client.id == client_id).first()
    if db_client:
        db.delete(db_client)
        db.commit()
    return db_client