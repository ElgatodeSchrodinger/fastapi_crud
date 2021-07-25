import bcrypt
from fastapi import APIRouter

from fastapi_crudrouter import SQLAlchemyCRUDRouter
#the following line of code are to import the user in our model and schema
from models import User as ModelUser
from models import Employee as ModelEmployee
from models import Client as ModelClient

from schema import UserCreate as SchemaUser
from schema import EmployeeCreate as SchemaEmployee
from schema import ClientCreate as SchemaClient

from schema import User as Users
from schema import Employee as Employees
from schema import Client as Clients


from database import get_db

user_router = SQLAlchemyCRUDRouter(
    schema=Users,
    create_schema=SchemaUser,
    db_model=ModelUser,
    db=get_db,
    prefix='/user'
)


employee_router = SQLAlchemyCRUDRouter(
    schema=Employees,
    create_schema=SchemaEmployee,
    db_model=ModelEmployee,
    db=get_db,
    prefix='/employee'
)


client_router = SQLAlchemyCRUDRouter(
    schema=Clients,
    create_schema=SchemaClient,
    db_model=ModelClient,
    db=get_db,
    prefix='/client'
)

# @router.post("/register", response_model=Users)
# async def create_user(user: SchemaUser):
#     hashed_password = bcrypt.hashpw(user.hashed_password.encode('utf-8'), bcrypt.gensalt())
#     user_dict = user.dict()
#     user_dict['hashed_password'] = hashed_password
#     User = ModelUser(**user_dict)
#     db.session.add(User)
#     db.session.commit()
#     db.session.refresh(User)
#     return User