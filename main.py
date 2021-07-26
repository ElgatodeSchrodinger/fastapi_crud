

from pydantic import BaseModel
from fastapi import FastAPI
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from router import employee_router, client_router, user_router, router, product_router
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()




# app.include_router(user_router)
app.include_router(employee_router)
# app.include_router(client_router)
app.include_router(product_router)
app.include_router(router)
