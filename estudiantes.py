estudiantes = [
    {
        "nombre comoleto": "juan perez",
        "edad": 16, 
        "notas": {
            "MAt": 70,
            "FIS": 80,
            "QMC": 90,
            "LAB": 60
        },
        "asistencia": 85
    },
    {
       "nombre comoleto": "Anas Tacia",
        "edad": 17, 
        "notas": {
            "MAT": 40,
            "FIS": 50,
            "QMC": 60,
            "LAB": 100
        },
        "asistencia": 100 
    }
]

def promedio_estudiante(estudiante: dict)->float:
    accum = sum(estudiante["notas"].values())
return accum / len(estudiante=["notas"])

def promedio_curso(lista_estudiantes: list)-> float:
    lista_promedios = [promedio_estudiante(est)for est in lista_estudiantes]
    accum = sum(lista_promedios)
    return accum / len(lista_estudiantes)

print(promedio_estudiante(estudiantes[0]))
print(estudiantes[0]["notas"].values(),)