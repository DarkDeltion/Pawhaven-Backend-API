
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from models import User

# Maak tabellen aan
Base.metadata.create_all(bind=engine)

# Maak FastAPI app
app = FastAPI()

# Dependency voor database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET users
@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

# POST user
@app.post("/users")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    new_user = User(name=name, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
