
'''
productos=[]
ag=0
def menu():
  global ag
  codigo="PF"
  opc = ("Nuevo Producto", "Listar Productos","Agregar inventario","Salir inventario" ,"Eliminar", "Consulta", "Salir")
  for i in range(len(opc)):
    print(str(i+1)+".- "+opc[i]+".")
  op=0
  while op<1 or op>len(opc):
    op = int(input("ingrese una opcion[1.."+str(len(opc))+"]:"))
  if op==1:
      codigo=codigo+str(ag+1)
      print("Codigo:" +str(codigo))
      nombre = input("Nombre:")
      precio = float(input("Precio:"))
      cantidad = float(input("Cantidad:"))
      productos.append([codigo,nombre,precio,cantidad])
      ag=ag+1
      input("Cualquier tecla para continuar..")
      menu()
  if op==2:
    print("Lista de productos")
    for i in range(len(productos)):
       print(str(productos[i][0])+" "+productos[i][1]+" "+str(productos[i][2])+" "+str(productos[i][3]))
    input("Cualquier tecla para continuar..")
    menu()

  if op==3:
    print("\t\tAgregar cantidad en productos")
    cod = input("Codigo:")
    pos=-1
    for i in range(len(productos)):
      if cod.upper()==productos[i][0]:
        pos=i
        break
    if pos!=-1:
      cad="Nombre:"+productos[pos][1]+"\nPrecio:"+str(productos[pos][2])+\
          "\nCantidad:"+str(productos[pos][3])
      print(cad)
      cantidad = int(input("Cantidad:"))
      productos[pos][3]=productos[pos][3]+cantidad
      print("Cantidad actual:"+str(productos[pos][3]))
    else:
      print("Codigo no existe!")
    input("Cualquier tecla para continuar..")
    menu()

  if op==4:
    print("\t\tSalida de productos")
    cod = input("Codigo:")
    pos=-1
    for i in range(len(productos)):
      if cod.upper()==productos[i][0]:
        pos=i
        break
    if pos!=-1:
      cad="Nombre:"+productos[pos][1]+"\nPrecio:"+str(productos[pos][2])+\
          "\nCantidad:"+str(productos[pos][3])
      print(cad)
      cantidad = int(input("Cantidad de salida:"))
      cant = productos[pos][3]-cantidad
      if cant<0:
        print("Proceso de inventario invalido!")
      else:
        productos[pos][3] = productos[pos][3] - cantidad
      print("Cantidad actual:"+str(productos[pos][3]))
    else:
        print("Codigo no existe!")
    input("Cualquier tecla para continuar..")
    menu()
  if op==5:
    print("\t\tEliminar Productos")
    cod = input("Codigo:")
    pos = -1
    for i in range(len(productos)):
      if cod.upper() == productos[i][0]:
        pos = i
        break
    if pos != -1:
      cad = "Nombre:" + productos[pos][1] + "\nPrecio:" + str(productos[pos][2]) + \
            "\nCantidad:" + str(productos[pos][3])
      print(cad)
      productos.pop(pos)
      print("Producto eliminado!")
    else:
      print("Codigo no existe!")
    input("Cualquier tecla para continuar..")
    menu()

  if op==6:
    print("\t\tConsulta en productos")
    cod = input("Codigo:")
    pos=-1
    for i in range(len(productos)):
      if cod.upper()==productos[i][0]:
        pos=i
        break
    if pos!=-1:
      cad="Nombre:"+productos[pos][1]+"\nPrecio:"+str(productos[pos][2])+\
          "\nCantidad:"+str(productos[pos][3])
      print(cad)
    else:
      print("Codigo no existe!")
    input("Cualquier tecla para continuar..")
    menu()


  if op==7:
    print("SAlir..")


menu()

'''
productos=[]
ag=0
op =1
opc = ("Nuevo Producto", "Listar Productos","Agregar inventario","Salir inventario" ,"Eliminar", "Consulta", "Salir")
while op>0 and op<len(opc):
    for i in range(len(opc)):
      print(str(i+1)+".- "+opc[i]+".")
    op=0
    while op<1 or op>len(opc):
      op = int(input("ingrese una opcion[1.."+str(len(opc))+"]:"))
    if op==1:
      codigo="PF"+str(ag+1)
      print("Codigo:" +str(codigo))
      nombre = input("Nombre:")
      precio = float(input("Precio:"))
      cantidad = float(input("Cantidad:"))
      productos.append([codigo,nombre,precio,cantidad])
      ag=ag+1
      input("Cualquier tecla para continuar..")

    if op==2:
      print("Lista de productos")
      for i in range(len(productos)):
        print(str(productos[i][0])+" "+productos[i][1]+" "+str(productos[i][2])+" "+str(productos[i][3]))
      input("Cualquier tecla para continuar..")

    if op==3:
      print("\t\tAgregar cantidad en productos")
      cod = input("Codigo:")
      pos=-1
      for i in range(len(productos)):
        if cod.upper()==productos[i][0]:
          pos=i
          break
      if pos!=-1:
          cad="Nombre:"+productos[pos][1]+"\nPrecio:"+str(productos[pos][2])+\
              "\nCantidad:"+str(productos[pos][3])
          print(cad)
          cantidad = int(input("Cantidad:"))
          productos[pos][3]=productos[pos][3]+cantidad
          print("Cantidad actual:"+str(productos[pos][3]))
      else:
          print("Codigo no existe!")
      input("Cualquier tecla para continuar..")


    if op==4:
      print("\t\tSalida de productos")
      cod = input("Codigo:")
      pos=-1
      for i in range(len(productos)):
        if cod.upper()==productos[i][0]:
          pos=i
          break
      if pos!=-1:
         cad="Nombre:"+productos[pos][1]+"\nPrecio:"+str(productos[pos][2])+\
              "\nCantidad:"+str(productos[pos][3])
         print(cad)
         cantidad = int(input("Cantidad de salida:"))
         cant = productos[pos][3]-cantidad
         if cant<0:
            print("Proceso de inventario invalido!")
         else:
            productos[pos][3] = productos[pos][3] - cantidad
         print("Cantidad actual:"+str(productos[pos][3]))
      else:
          print("Codigo no existe!")
      input("Cualquier tecla para continuar..")

    if op==5:
      print("\t\tEliminar Productos")
      cod = input("Codigo:")
      pos = -1
      for i in range(len(productos)):
        if cod.upper() == productos[i][0]:
            pos = i
            break
      if pos != -1:
          cad = "Nombre:" + productos[pos][1] + "\nPrecio:" + str(productos[pos][2]) + \
                "\nCantidad:" + str(productos[pos][3])
          print(cad)
          productos.pop(pos)
          print("Producto eliminado!")
      else:
          print("Codigo no existe!")
      input("Cualquier tecla para continuar..")

    if op==6:
      print("\t\tConsulta en productos")
      cod = input("Codigo:")
      pos=-1
      for i in range(len(productos)):
        if cod.upper()==productos[i][0]:
          pos=i
          break
      if pos!=-1:
        cad="Nombre:"+productos[pos][1]+"\nPrecio:"+str(productos[pos][2])+\
              "\nCantidad:"+str(productos[pos][3])
        print(cad)
      else:
        print("Codigo no existe!")
      input("Cualquier tecla para continuar..")

      if op==7:
        print("SAlir..")

