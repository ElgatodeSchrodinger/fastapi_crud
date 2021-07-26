

from pydantic import BaseModel
from fastapi import FastAPI
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from router import employee_router, client_router, user_router, router, product_router
from database import Base, engine
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()


origins = [
    "http://localhost:5000",
    "http://0.0.0.0:8080",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# app.include_router(user_router)
app.include_router(employee_router)
# app.include_router(client_router)
app.include_router(product_router)
app.include_router(router)
