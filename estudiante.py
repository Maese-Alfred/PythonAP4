from nodo import LinkedList
from materia import Materia
import re

class Estudiante:
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula
        self.materias = LinkedList()

    def agregarMateria(self, nombre, calificacion):
        if not re.match(r'^(100|[1-9]?[0-9])$', str(calificacion)):
            raise ValueError("La calificación debe ser un número entero entre 0 y 100.")
        materia = Materia(nombre, calificacion)
        self.materias.insertarAlFinal(materia)

    def __str__(self):
        return f"{self.nombre} ({self.matricula})"