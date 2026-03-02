
from fastapi import FastAPI
from db.database import engine, Base

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Register your routers here, for example:
# from api.routes import example
# app.include_router(example.router)