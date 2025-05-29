class Materia:
    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion

    def __str__(self):
        return f"{self.nombre} ({self.calificacion})"
    
    def __repr__(self):
        return f"Materia(nombre={self.nombre}, calificacion={self.calificacion})"