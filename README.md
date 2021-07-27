# fastapi Store

Requerimientos:
 - Python 3.7 >
 - pip

Pasos para instalarlo:

1. Clonar el repositorio:

```.shell script
    git clone https://github.com/ElgatodeSchrodinger/fastapi_crud.git
```
  
2. Crear y activar el entorno virtual:

- Para crear el entorno puede usar virtualenv
```.shell script
    virtualenv env -p python3
```
- O también con el módulo venv:
```.shell script
    python3 -m venv env
```
- Para activar el entorno
```.shell script
   source env/bin/activate 
```
   
3. Instalar los requerimientos:
```.shell script
    pip install -r requirements.txt
```

4. Ejecutar la aplicacion
```.shell script
    uvicorn main:app
```

La aplicacion estar corriendo en el localhost:8000

Si es la primera que lo corre la aplicacion , se creara la base de datos de forma automatica
 en sqllite llamada app.db.