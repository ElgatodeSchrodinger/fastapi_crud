import bcrypt
from fastapi import APIRouter, UploadFile, File
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from sqlalchemy.sql import select
from database import Session
from typing import List


from schema import Login, SaleCreate
from database import get_db
from fastapi import Depends
#the following line of code are to import the user in our model and schema
from models import DetalleVenta, User as ModelUser
from models import Employee as ModelEmployee
from models import Client as ModelClient
from models import Producto as ModelProducto
from models import Venta as ModelVenta
from models import DetalleVenta as ModelDetalleVenta

from schema import UserCreate as SchemaUser
from schema import EmployeeCreate as SchemaEmployee
from schema import ClientCreate as SchemaClient
from schema import ProductCreate as SchemeProduct

from schema import EmployeeUpdate

from schema import User as Users
from schema import Employee as Employees
from schema import Client as Clients
from schema import Product as Products

from schema import SaleBase as SaleSchema

from schema import SaleUpdate


from schema import Sale
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
    update_schema=EmployeeUpdate,
    db_model=ModelEmployee,
    db=get_db,
    prefix='/employee',
    create_route=False,
    update_route=False,
    delete_all_route=False,
)


client_router = SQLAlchemyCRUDRouter(
    schema=Clients,
    create_schema=SchemaClient,
    db_model=ModelClient,
    db=get_db,
    prefix='/client'
)

product_router = SQLAlchemyCRUDRouter(
    schema=Products,
    create_schema=SchemeProduct,
    db_model=ModelProducto,
    db=get_db,
    prefix='/producto'
)


@employee_router.delete('{/{item_id}}')
def delete_employee(id_employee: int, db: Session = Depends(get_db)):

    employee = db.query(ModelEmployee).filter(ModelEmployee.id == id_employee).first()
    db.query(ModelUser).filter(ModelUser.id == employee.id_user).delete()
    db.commit()
    employee.delete()
    db.commit()

# import uuid
# IMAGEDIR = "fastapi-images/"

# @product_router.post('')
# def create_product(product: SchemeProduct, file: UploadFile = File(...), db: Session = Depends(get_db)):

#     print(**product.dict())
#     file.filename = f"{uuid.uuid4()}.jpg"
#     contents = file.read()  # <-- Important!

#     # example of how you can save the file
#     with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
#         f.write(contents)

    
#     Product = ModelProducto(image=f"{IMAGEDIR}{file.filename}", **product)


#     db.add(Product)
#     db.commit()
#     db.refresh(Product)
#     return Product





router = APIRouter()



@router.post("/register")
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
    id_val = None
    if type_user == "empleado":
        Employee = ModelEmployee(**person_data)
        db.add(Employee)
        db.commit()
        db.refresh(Employee)
        id_val = Employee.id
    elif type_user == "cliente":
        Client = ModelClient(**person_data)
        db.add(Client)
        db.commit()
        db.refresh(Client)
        id_val = Client.id
    key_val = "id_" + type_user
    return {
        'id': User.id,
        'nombre': User.nombre,
        'estado': User.estado,
        key_val: id_val
    }

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
                "message": "Perfil no definido"}
    else:
        return {"message": "Usuario o contraseña no coinciden"}


@router.post("/venta")
def registrar_venta(request: SaleCreate, db: Session = Depends(get_db)):

    venta_data = request.dict()

    product_sale = {}

    for detalle in venta_data['detalle_venta']:
        Product = db.query(ModelProducto).filter(ModelProducto.id == detalle['id_product']).first()
        product_sale[Product.id] = detalle['cantidad'], Product.stock, Product
    
    product_avaiable = all([product[0] <= product[1] for product in product_sale.values() ])

    if product_avaiable:
        lines = venta_data.pop('detalle_venta', [])
        # print(venta_data)
        try:
            Venta = ModelVenta(**venta_data)
            db.add(Venta)
            db.commit()
            db.refresh(Venta)
        except:
            print("Error al crear venta")

        lines_ids = []
        for line in lines:
            line_data = line
            line_data['id_venta'] = Venta.id
            DetalleVenta = ModelDetalleVenta(**line_data)
            db.add(DetalleVenta)
            db.commit()
            db.refresh(DetalleVenta)

            if DetalleVenta.id_product in product_sale.keys():
                data_product = product_sale[DetalleVenta.id_product]
                data_product[2].stock = data_product[1] - data_product[0]
                db.commit()
            lines_ids.append(DetalleVenta.id)

        # print(request.detalle_venta)
        return {
            "id_venta": Venta.id,
            "ids_detallesventa": lines_ids
        }
    else:
        return {
            "message": "No se tiene stock suficiente para la venta"
        }


# @router.get("/venta")
# def get_all_ventas(db: Session = Depends(get_db)):
#     res = db.query(ModelVenta).all()
#     print(res)
#     list_res = []
#     for venta in res:
#         print(type(venta))
#         venta_data = venta
#         venta_data['detalleVenta'] = db.query(ModelDetalleVenta).filter(ModelDetalleVenta.id_venta==venta.id).all()
#         list_res.append(venta_data)


#     return list_res

@router.get("/venta")
def get_all_ventas(db: Session = Depends(get_db)):
    res = db.query(ModelVenta).all()
    return res

@router.put("/venta/{id_venta}/{id_empleado}")
def update_estado(id_venta: int, id_empleado: int, payload: SaleUpdate, db: Session = Depends(get_db)):
    res = db.query(ModelVenta).filter(ModelVenta.id==id_venta).first()
    res.estado = payload.estado
    if payload.id_empleado:
        res.id_empleado = id_empleado
    db.commit()
    return res

@router.put("/empleado/{id_empleado}")
def update_estado(id_empleado: int, payload: EmployeeUpdate, db: Session = Depends(get_db)):
    res = db.query(ModelEmployee).filter(ModelEmployee.id==id_empleado).first()

    # fields = ('nombres', 'apellidos', 'dni', 'genero', 'celular', 'direccion', 'fecha_nacimiento')
    res.nombres = payload.nombres if payload.nombres else res.nombres
    print(res.nombres)
    res.apellidos = payload.apellidos if payload.apellidos else res.apellidos
    print(res.apellidos)
    res.dni = payload.dni if payload.dni else res.dni
    res.genero = payload.genero if payload.genero else res.genero
    res.celular = payload.celular if payload.celular else res.celular
    res.email = payload.email if payload.email else res.email
    res.direccion = payload.direccion if payload.direccion else res.direccion
    res.fecha_nacimiento = payload.fecha_nacimiento if payload.fecha_nacimiento else res.fecha_nacimiento
    db.commit()
    return res