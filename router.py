import bcrypt
from fastapi import APIRouter
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from sqlalchemy.sql import select
from database import Session

from schema import Login
from database import get_db
from fastapi import Depends
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

router = APIRouter()



@router.post("/register", response_model=Users)
async def create_user(user: SchemaUser, db: Session = Depends(get_db)):
    hashed_password = bcrypt.hashpw(user.clave.encode('utf-8'), bcrypt.gensalt())
    user_dict = user.dict()
    user_dict['clave'] = hashed_password
    
    user_data = {}
    person_data = {}
    user_fields = ('nombre', 'clave', 'estado')
    for field in user_dict.keys():
        if field in user_fields:
            user_data[field] = user_dict[field]
        else:
            person_data[field] = user_dict[field]

    User = ModelUser(**user_data)

    db.add(User)
    db.commit()
    db.refresh(User)

    type_user = person_data.pop('tipo', None)
    person_data['id_user'] = User.id
    
    # print(person_data)

    if type_user == "empleado":
        Employee = ModelEmployee(**person_data)
        db.add(Employee)
        db.commit()
        db.refresh(Employee)
    elif type_user == "cliente":
        Client = ModelClient(**person_data)
        db.add(Client)
        db.commit()
        db.refresh(Client)

    return User

@router.post("/login")
def login(request: Login, db: Session = Depends(get_db)):
    print(type(ModelUser))
    nombre = request.usuario
    clave = request.clave

    user = db.query(ModelUser).filter(ModelUser.nombre == nombre).first()

    if user and bcrypt.checkpw(clave.encode('utf-8'), user.clave):
        is_employee = db.query(ModelEmployee).filter(ModelEmployee.id_user == user.id).first()
        is_client = db.query(ModelClient).filter(ModelClient.id_user == user.id).first()
        if is_employee:
            return {
                "nombre": is_employee.nombres,
                "tipousuario": "empleado",
                "id_user": user.id,
                "id": is_employee.id,

            }
        elif is_client:
            return {
                "nombre": is_client.nombres,
                "tipousuario": "cliente",
                "id_user": user.id,
                "id": is_client.id,
            }
        else:
            return {
                "nombre": user.nombre,
                "id_user": user.id,
                "message": "Usuario o contraseña no coinciden"}
    else:
        return {"message": "Usuario o contraseña no coinciden"}

    
    # user = db.execute(select(ModelUser).where(ModelUser.c.id == 1))
    # res_user = Session.query(ModelUser).filter_by(**request).one()
    # return users