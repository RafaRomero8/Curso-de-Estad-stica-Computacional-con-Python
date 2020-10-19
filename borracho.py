import random

class Borracho:

    def __init__(self, nombre):#constructor
        self.nombre = nombre


class BorrachoTradicional(Borracho):#herenciaa

    def __init__(self, nombre):#genera constructor
        super().__init__(nombre)#referencia a la funcion con super()

    def camina(self):
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])#coordenadas en el plano se mueve a la derecha ,izq,etc.
             #random.choice permite geneerar de manera aleatoria con la misma probailidad