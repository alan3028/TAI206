from fastapi import FastAPI,status,HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
 
 
  # seguridad con HTTPBasic
security = HTTPBasic()

def verificar_usuario(credentials: HTTPBasicCredentials = Depends(security)):
    usuarioAuth= secrets.compare_digest(credentials.username, "admin")
    contrasenaAuth= secrets.compare_digest(credentials.password, "1234")
    
    if not(usuarioAuth and contrasenaAuth):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales no validas",
        )
        
    return credentials.username