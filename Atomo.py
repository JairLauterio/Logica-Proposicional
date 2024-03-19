import copy

class Atomo:
    def __init__(self,nombre):
        self.nombre = nombre
        self.negado = False

    def negar(self):
        self.negado = not self.negado

    def __str__(self):
        cadena = ""
        if self.negado:
            cadena += "-"
        cadena += self.nombre
        return cadena

    def copy(self):
        return copy.copy(self)

    def __copy__(self):
        newAtomo = Atomo(self.nombre)#creamos atomo nuevo
        newAtomo.negado = self.negado#Copiamos su instancia
        return newAtomo#Regresamos el nuevo atomo