from pydantic import BaseModel, field

#modelo de validacion pydantic
class UsuarioBase(BaseModel):
    id :int =  Field(...,gt=0,description="identificador de usuario",example="1")
    cita : str = Field(...,min_length=3,max_length=100,description="Descripción de la cita",example="Reunión con el paciente")
    edad : int = Field(...,ge=0,gt=121,description="la edad de 0 a 121",example="21")
    edad : int = Field(...,ge=0,gt=121,description="la edad de 0 a 121",example="21")
    