from fastapi import FastAPI
from app.routes import auth_routes, contacts_routes
from app.db.dataBase import engine
from app.models import user_model


app = FastAPI(
    title="ContactDesk API",
    description="API to manage contacts, users, and authentication",
    version="1.0.0"
)

app.include_router(auth_routes.router)
app.include_router(contacts_routes.router)

user_model.Base.metadata.create_all(bind=engine)