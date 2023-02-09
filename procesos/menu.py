def getMenu(tupla):
    for i in range(len(tupla)):
        print(str(i+1)+".- "+tupla[i]+".")
    op = 0
    while op<1 or op>len(tupla):
        op=int(input("Ingrese una opcion[1.."+str(len(tupla))+"]:"))
    return op