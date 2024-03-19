import re

from Atomo import Atomo
from Clausula import Clausula
from Formula import Formula

archivo=open("datos/formula1.txt")
lineas = archivo.readlines()

def infijo2postfijo(infijo):
    postfijo = []
    pila = []
    for ch in infijo:
        p=getPrioridad(ch)
        if p == -1:
            pila.append(ch)
        elif p == -2:
    #Extraer el elemento del tope de la pila e introducir a postfijo,
    # hasta encontrar (  pero no introducir el paréntesis a postfijo.
            while (len(pila) > 0):
                tope = pila.pop()
                if (tope != "("):
                    postfijo.append(tope)
                else:
                    break
        elif p > 0:
    # la pila esta vacı́a or ch tiene
    # más alta prioridad que el elemento del tope de la pila
            if len(pila) == 0 or p > getPrioridad(pila[-1]):
                pila.append(ch)
    # Extraer el elemento del tope de la pila e introducir a postfijo.
    # Y repetir la comparación con el nuevo tope
            else:
                while len(pila)>0 and p < getPrioridad(pila[-1]):
                    tope = pila.pop()
                    postfijo.append(tope)
                pila.append(ch)
        else:
            postfijo.append(ch)
    while len(pila) > 0:
        postfijo.append(pila.pop())
    return postfijo

def getPrioridad(a):
    if (a == "|"):
        return 1
    if (a == "&"):
        return 2
    if (a == ">"):
        return 3
    if (a == "="):
        return 4
    if (a == "-"):
        return 5
    if (a == "("):
        return -1
    if (a == ")"):
        return -2
    else:
        return 0

def evaluar(postfijo):
    pila=[]
    for ch in postfijo:
        p=getPrioridad(ch)
        if p==0: #Si es igual a 0 es un operando y se convierte en formula y mete a pila
            a = Atomo(ch)
            c = Clausula()
            f = Formula()
            c = c.orAtomo(a)
            c = f.andClausula(c)
            pila.append(c)
        elif p == 1: #Si es igual a 1 es or y se convierte en formula y mete a pila
            b = pila.pop()
            a = pila.pop()
            c = a.orFormula(b)
            pila.append(c)
        elif p == 2: #2 es igual a And y se convierte en formula y mete a pila
            b = pila.pop()
            a = pila.pop()
            c = a.andFormula(b)
            pila.append(c)
        elif p == 3: #3 es entonces y se convierte en formula y mete a pila
            b = pila.pop()
            a = pila.pop()
            a = a.negarFormula()
            c = a.orFormula(b)
            pila.append(c)
        elif p == 4: #4 es Si solo Si y se convierte en formula y mete a pila
            b = pila.pop()
            a = pila.pop()
            an = a.negarFormula()
            bn = b.negarFormula()
            c = a.orFormula(bn)
            d = b.orFormula(an)
            c = c.andFormula(d)
            pila.append(c) #No esta completo
        elif p == 5: #4 es Not y convierte en formula y mete a pila
            a = pila.pop()
            c = a.negarFormula()  #Falta por hacer
            pila.append(c)
    return pila.pop() #No esta completo

for linea in lineas:
    print(f'Linea: {linea}')
    infijo = re.findall("(\\w+|\\||\\&|\\>|\\-|\\(|\\)|\\=)",linea)
    #infijo = re.findall("(\w+|\||\&|\>|\-|\(|\)|\=)", linea)
    print(f'Infijo: {infijo}')
    postfijo = infijo2postfijo(infijo)
    print(f'Postfijo: {postfijo}')
    fnc = evaluar(postfijo)
    print(f'FNC: {fnc}')

#c = Clausula()
#a = Atomo("a")
#c = c.orAtomo(a)
#a.negar()
#c = c.orAtomo(a)

#print(c)

#a = Atomo("A")
#b = Atomo("B")
#b.negar()
#c=Atomo("C")
#c1 = Clausula()
#c2 = Clausula()

#c1=c1.orAtomo(a)
#c1=c1.orAtomo(b)
#c1=c1.orAtomo(c)
#f1=c1.negar()
#c2=c2.orAtomo(c)
##f1=c1.andAtomo(b)
#f1 = c1.andClausula(c2)

#print(f1)