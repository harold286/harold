from pydantic import BaseModel

class asignatura(BaseModel):
    nombre: str
    estudiantes: int