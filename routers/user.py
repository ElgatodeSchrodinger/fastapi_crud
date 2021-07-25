# import bcrypt
# from fastapi import APIRouter
# from fastapi_sqlalchemy import db
# from fastapi_crudrouter import SQLAlchemyCRUDRouter
# from .models import User, Employee, 
# #the following line of code are to import the user in our model and schema
# from model import User as ModelUser
# from schema import UserCreate as SchemaUser
# from schema import User as Users

# router = SQLAlchemyCRUDRouter(
#     schema=Potato,
#     create_schema=PotatoCreate,
#     db_model=PotatoModel,
#     db=get_db,
#     prefix='potato'
# )

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