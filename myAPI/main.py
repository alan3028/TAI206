#Importaciones
from typing import Optional
from fastapi import FastAPI
import asyncio

#Inicializacion
app = FastAPI(
    titulo='Mi primer API',
    description='Alan santiago ',
    version= '1.0'
)
#bd 
usuarios=[
    {"id":1,"nombre":"Alan","edad":22},
    {"id":2,"nombre":"alondra","edad":22},
    {"id":3,"nombre":"ximena","edad":21},
]

#Endpoints
@app.get("/", tags=['Inicio'])
async def holamundo():
    return {"mensaje":" Hola mundo FastAPI"}

@app.get("/bienvenido", tags=['Inicio'])
async def bienvenido():
    return {"mensaje":" bienvenido a tu  API REST"}

@app.get("/v1/calificaciones", tags=['Asincronia'])
async def calificaciones():
    await asyncio.sleep(6)
    return {"mensaje":"Tu calificaciones es TAI es 10"}

@app.get("/v1/usuario_op/{id}", tags=['parametro Obligatorio'])
async def consultausuarios(id:int):
    await asyncio.sleep(3)
    return {"usuario encontrado ":id }

@app.get("/v1/usuario_op/", tags=['parametro Opcional'])
async def consultaOp(id:Optional[int]=None):
    await asyncio.sleep(3)
    if id is not None:
        for usuario in usuarios:
            if usuario ["id"]  == id:
                     return {"usuario encontrado ":id , "datos":usuario}
        return {"mensaje":"usuario encontrado " }
    else:
      return{"Aviso":"No se proporciono Id "}