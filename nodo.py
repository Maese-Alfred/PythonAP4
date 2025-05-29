class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertarAlFinal(self, data):
        nuevo = Node(data)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo

    def recorrer(self):
        actual = self.head
        while actual:
            yield actual.data
            actual = actual.next

    def estaVacia(self):
        return self.head is None