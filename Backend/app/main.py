from fastapi import FastAPI
from app.db.dataDase import engine

app = FastAPI(
    title="ContactDesk API",
    description="API to manage contacts, users, and authentication",
    version="1.0.0"
)

