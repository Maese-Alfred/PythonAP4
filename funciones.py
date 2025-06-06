from nodo import *

def calcularPromedioRecursivo(iterator):
    materia = next(iterator, None)
    if materia is None:
        return 0, 0
    suma, cantidad = calcularPromedioRecursivo(iterator)
    return suma + materia.calificacion, cantidad + 1

def eliminarMateriasReprobadas(linked_list):
    nueva_lista = LinkedList()
    for materia in linked_list.recorrer():
        if materia.calificacion >= 60:
            nueva_lista.insertarAlFinal(materia)
    return nueva_lista

def mostrarMaterias(linked_list):
    if linked_list.estaVacia():
        return "No hay materias."
    resultado = []
    for materia in linked_list.recorrer():
        resultado.append(str(materia))
    return "\n".join(resultado)

def buscarMateriaBinaria(materias_ordenadas, nombre):
    if not materias_ordenadas:
        return None
    mid = len(materias_ordenadas) // 2
    if materias_ordenadas[mid].nombre == nombre:
        return materias_ordenadas[mid]
    elif materias_ordenadas[mid].nombre < nombre:
        return buscarMateriaBinaria(materias_ordenadas[mid + 1:], nombre)
    else:
        return buscarMateriaBinaria(materias_ordenadas[:mid], nombre)

def ordenarPorCountingSort(linked_list):
    materias = list(linked_list.recorrer())
    max_val = 100
    min_val = 1
    rango = max_val - min_val + 1
    conteo = [0] * rango

    for num in materias:
        conteo[num - min_val] += 1

    for i in range(1, rango):
        conteo[i] += conteo[i - 1]

    salida = [0] * len(materias)

    for num in reversed(materias):
        salida[conteo[num - min_val] - 1] = num
        conteo[num - min_val] -= 1

    for i in range(len(materias)):
        materias[i] = salida[i]
    ordenadas = LinkedList()
    for materia in materias:
        ordenadas.insertarAlFinal(materia)
    return ordenadas