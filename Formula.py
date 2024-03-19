class Formula:
    def __init__(self):
        self.clausulas = []

    def andClausula(self, clausula):
        f=Formula()
        for c in self.clausulas:
            f.clausulas.append(c.__copy__())
        f.clausulas.append(clausula.__copy__())
        return f

#OrFormula
#AndFormula
#NegarFormula

    def andFormula(self, formula):
        f = Formula()
        for c in self.clausulas:
            f.clausulas.append(c.__copy__())
        for c in formula.clausulas:
            f.clausulas.append(c.__copy__())
        return f

    def orFormula(self, formula):
        f=Formula()
        for c in self.clausulas:
            for c2 in formula.clausulas:
                f.clausulas.append(c.orClausula(c2))
        return f

    def negarFormula(self):
        f=Formula()
        for c in self.clausulas:
            negated_clause = c.negar()
            f=f.andFormula(negated_clause)
        return f
    def __str__(self):
        cadena = "["
        for indice, clausulas in enumerate(self.clausulas):
            cadena += clausulas.__str__()
            if indice != len(self.clausulas) - 1:
                cadena += " & "
        cadena += "]"
        return cadena