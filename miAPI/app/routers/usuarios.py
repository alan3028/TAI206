from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import Optional

# Importaciones de tu proyecto
from app.models.usuario import UsuarioBase
from app.data.db import get_db
from app.data.usuario import Usuario as usuarioDB
from app.security.auth import verificar_Peticion

router = APIRouter(
    prefix="/v1/usuarios",
    tags=["CRUD HTTP"]
)


@router.get("/")
async def consultaUsuarios(db: Session = Depends(get_db)):
    usuarios_db = db.query(usuarioDB).all()
    return {
        "status": "200",
        "total": len(usuarios_db),
        "data": usuarios_db
    }


@router.get("/{id}")
async def obtenerUsuarioPorId(id: int, db: Session = Depends(get_db)):
    usuario = db.query(usuarioDB).filter(usuarioDB.id == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario


@router.post("/", status_code=status.HTTP_201_CREATED)
async def agregarUsuarios(usuarioP: UsuarioBase, db: Session = Depends(get_db)):
    nuevoUsuario = usuarioDB(nombre=usuarioP.nombre, edad=usuarioP.edad)
    db.add(nuevoUsuario)
    db.commit()
    db.refresh(nuevoUsuario)
    return {
        "mensaje": "Usuario Agregado",
        "datos": nuevoUsuario
    }


@router.put("/{id}", status_code=status.HTTP_200_OK)
async def actualizarUsuario(id: int, usuarioP: UsuarioBase, db: Session = Depends(get_db)):
    usuario_query = db.query(usuarioDB).filter(usuarioDB.id == id)
    usuario_existente = usuario_query.first()

    if not usuario_existente:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Actualizamos los campos
    usuario_query.update({
        "nombre": usuarioP.nombre,
        "edad": usuarioP.edad
    })
    db.commit()
    
    return {
        "mensaje": "Usuario actualizado completamente",
        "datos": usuario_query.first()
    }


@router.patch("/{id}", status_code=status.HTTP_200_OK)
async def actualizarParcialUsuario(id: int, nombre: Optional[str] = None, edad: Optional[int] = None, db: Session = Depends(get_db)):
    usuario_query = db.query(usuarioDB).filter(usuarioDB.id == id)
    usuario_existente = usuario_query.first()

    if not usuario_existente:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Solo actualizamos los campos que no sean None
    update_data = {}
    if nombre is not None: update_data["nombre"] = nombre
    if edad is not None: update_data["edad"] = edad

    usuario_query.update(update_data)
    db.commit()
    
    return {
        "mensaje": "Usuario actualizado parcialmente",
        "datos": usuario_query.first()
    }


@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def eliminarUsuario(id: int, db: Session = Depends(get_db), usuarioAuth: str = Depends(verificar_Peticion)):
    usuario_query = db.query(usuarioDB).filter(usuarioDB.id == id)
    usuario_existente = usuario_query.first()

    if not usuario_existente:
        raise HTTPException(status_code=404, detail="Usuario no encontrado para eliminar")

    db.delete(usuario_existente)
    db.commit()
    
    return {
        "mensaje": f"Usuario con ID {id} eliminado correctamente por {usuarioAuth}"
    }