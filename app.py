from fastapi import FastAPI
from asignatura import asignatura

app = FastAPI()

cursos = {
    'programacion':{'fundamentos':15, 'POO':20},
    'matematicas': {'matEspeciales':20, 'calculoVect':25}
}

@app.get("/")
async def root():
    return{
        "message":"Hola mundo"
    }

@app.get("/cursos")
def listCursos():
    return cursos

@app.get("/cursos/{tipo}")
def tipoCurso(tipo:str):
    return {
        "asignaturas":cursos[tipo].items()
    }

@app.post("/validar-estudiantes")
def asignatura(data:asignatura):
    data = data.model_dump()
    nEstudiantes = data["estudiantes"]
    if(nEstudiantes > 20):
        return{
            'nEstudiantes':nEstudiantes,
            'accion': 'Nuevo Curso'
        }
    else: 
        return{
            'nEstudiantes':nEstudiantes,
            'accion': 'Unico curso'
        }