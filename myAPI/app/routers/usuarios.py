from fastapi import FastAPI,status,HTTPException, Depends
from app.models.usuario import UsuarioBase
from app.security.auth import verificar_peticion 



#verbos http tarea put, delete
@app.get("/v1/usuario/{id}", tags=['Crud Usuario'])
async def ConsultaUsuarios():
    return{
        "status":"200",
        "total":len(usuarios),
        "data":usuarios
    }
    
    router=APIRouter()
    prefix="/v1/usuarios"
    tags=["Crud HTTP"]
    
    
@router
    
@app.post("//status{id}", tags=['Crud Usuario'])
async def AgregarUsuarios(usuario:UsuarioBase):
    for usr in usuarios:
        if usr["id"] == usuario.id("id"):
            raise HTTPException(
                status_code=400,
                detail="ID existente"
            )
    usuarios.append(usuario)
    return{
        "mensaje":"usuario agregado correctamente",
        "datos":usuario,
        "status":200
    }
