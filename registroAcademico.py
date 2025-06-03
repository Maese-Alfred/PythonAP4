from estudiante import Estudiante
from funciones import *
from nodo import LinkedList
from materia import Materia

from estudiante import Estudiante
from funciones import *
from nodo import LinkedList

def obtenerMaterias():
    lista = LinkedList()
    while True:
        nombre = input("Nombre de la materia (o 'fin' para terminar): ")
        if nombre.lower() == 'fin':
            break
        try:
            calificacion = int(input(f"Calificación de {nombre}: "))
            if 0 <= calificacion <= 100:
                lista.insertarAlFinal(Materia(nombre, calificacion))
            else:
                print("Debe ser entre 0 y 100.")
        except ValueError:
            print("Entrada inválida.")
    return lista

def main():
    estudiantes = LinkedList()

    while True:
        print("\nMenú:")
        print("1. Agregar estudiante")
        print("2. Ver estudiantes")
        print("3. Calcular promedio")
        print("4. Eliminar materias reprobadas")
        print("5. Buscar materia")
        print("6. Ordenar materias por calificación")
        print("0. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            matricula = input("Matrícula: ")
            est = Estudiante(nombre, matricula)
            materias = obtenerMaterias()
            for m in materias.recorrer():
                est.agregarMateria(m.nombre, m.calificacion)
            estudiantes.insertarAlFinal(est)

        elif opcion == "2":
            if estudiantes.estaVacia():
                print("No hay estudiantes.")
            for est in estudiantes.recorrer():
                print(f"\n{est}")
                print(mostrarMaterias(est.materias))

        elif opcion == "3":
            for est in estudiantes.recorrer():
                it = iter(est.materias.recorrer())
                suma, cantidad = calcularPromedioRecursivo(it)
                promedio = suma / cantidad if cantidad else 0
                print(f"{est} - Promedio: {promedio:.2f}")

        elif opcion == "4":
            for est in estudiantes.recorrer():
                est.materias = eliminarMateriasReprobadas(est.materias)
                print(f"{est} - Materias aprobadas:")
                print(mostrarMaterias(est.materias))

        elif opcion == "5":
            nombre_materia = input("Materia a buscar: ")
            for est in estudiantes.recorrer():
                materias = list(est.materias.recorrer())
                materias.sort(key=lambda m: m.nombre)
                resultado = buscarMateriaBinaria(materias, nombre_materia)
                if resultado:
                    print(f"{est} tiene {resultado}")
                else:
                    print(f"{est} no tiene {nombre_materia}")

        elif opcion == "6":
            for est in estudiantes.recorrer():
                est.materias = ordenarPorCountingSort(est.materias)
                print(f"{est} - Materias ordenadas:")
                print(mostrarMaterias(est.materias))

        elif opcion == "0":
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()