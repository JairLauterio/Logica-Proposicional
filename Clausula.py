from Formula import Formula


class Clausula:
    def __init__(self):
        self.atomos=[]

    def orAtomo(self, atomo):
        c = Clausula()
        for a in self.atomos:
            c.atomos.append(a.__copy__())
        if self.comparate(atomo):
            c.atomos.append(atomo.__copy__())
        return c

    def comparate(self,atomo):
        for a in self.atomos:
            if atomo.nombre == a.nombre:
                if atomo.negado == a.negado:
                    return False
        return True


    def orClausula(self, clausula):
        c = Clausula()
        for atomo in self.atomos:
            c.atomos.append(atomo.__copy__())
        for atomo in clausula.atomos:
            #atomo_copy = atomo.copy()
            #self.atomos.append(atomo_copy)
            c.atomos.append(atomo.__copy__())
        return c



    def andAtomo(self, atomo):
        f = Formula()
        f=f.andClausula(self.__copy__())
        c = Clausula()
        c = c.orAtomo(atomo.__copy__())
        f=f.andClausula(c)
        return f

    def andClausula(self,clausula):
        f = Formula()
        f = f.andClausula(self)
        f = f.andClausula(clausula)
        return f

    def negar(self):
        f=Formula()
        for atomo in self.atomos:
            c = Clausula()
            a = atomo.__copy__()
            a.negar()
            c.atomos.append(a)
            f = f.andClausula(c)
        return f
    def __str__(self):
        cadena = "("
        for indice , atomo in enumerate(self.atomos):
            cadena += atomo.__str__()
            #cadena += "("
            #cadena += str(id(atomo)) #Direccion de memoria
            #cadena += ")"
            if indice != len(self.atomos)-1:
                cadena += " | "
        cadena+=")"
        return cadena

    def __copy__(self):
        c=Clausula()
        for atomo in self.atomos:
            c.atomos.append(atomo.__copy__())
        return c