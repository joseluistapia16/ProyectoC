class Input:

    def inputInt(self,cadena):
        valor = -1
        while valor<0:
            try:
                valor = int(input(cadena))
            except:
                valor=-1
        return valor

    def inputFloat(self,cadena):
        valor = -1
        while valor<0:
            try:
                valor = float(input(cadena))
            except:
                valor=-1
        return valor







def getSubtotal(precio,cantidad):
    return (precio*cantidad)

def getIva(subtotal):
    return (subtotal*0.12)

def getTotal(subtotal,iva):
    return (subtotal+iva)

def getResult(subtotal,iva,total):
    resultado = "Subtotal:"+str(round(subtotal,2))+\
                "\nIva:"+str(round(iva,2))+\
                "\nTotal a pagar:"+str(round(total,2))
    return resultado

def getPromedio(n1,n2):
    return ((n1+n2)/2)

def getEstado(promedio):
    if promedio<0 or promedio>10:
        return "Valor incorrecto!"
    else:
        if promedio>=0 and promedio<7:
            return "Reprobado"
        if promedio>=7 and promedio<=10:
            return "Aprobado"

def getEtapa(edad):
    if edad<0:
        return "Valor invalido!"
    else:
        if edad>=0 and edad<11:
            return "Infante"
        if edad>10 and edad<18:
            return "Adolescente"
        if edad>17 and edad<26:
            return "Joven"
        if edad>25 and edad<65:
            return "Adulto"
        if edad>64:
            return "Adulto mayor!"

def getSuma(x,y):
    return (x+y)

def getControl(valor,lista):
    res = False
    for i in range(len(lista)):
        if valor==lista[i]:
           res = True
           break
    return res
