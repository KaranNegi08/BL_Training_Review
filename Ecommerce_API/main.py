from fastapi import FastAPI
from routers.router import router
from db import Base, engine
app= FastAPI()

Base.metadata.create_all(bind=engine)



app.include_router(router, prefix="/ecommerce", tags=["Ecommerce API"])

