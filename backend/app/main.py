from fastapi import FastAPI
from .database import Base, engine
from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is running 🚀"}