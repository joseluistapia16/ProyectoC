class Operacion:

    def saludo(self,cadena):
        return cadena
    def presentacion(self):
        print("OPeracion ")
        print("Multiherencia")

    def getProduct(self,cod,lista):
        obj = None
        for i in range(len(lista)):
            if cod== lista[i].getCodigo():
                obj = lista[i]
                break
        return obj

    def getProductPos(self,cod, lista):
        pos = -1
        for i in range(len(lista)):
            if cod== lista[i].getCodigo():
                pos = i
                break
        return pos

    def getClient(self,ruc,lista):
        obj = None
        for i in range(len(lista)):
            if ruc== lista[i].getRuc():
                obj = lista[i]
                break
        return obj

    def getClientPos(self,ruc,lista):
        pos = -1
        for i in range(len(lista)):
            if ruc== lista[i].getRuc():
                pos = i
                break
        return pos


class Producto:

    def __init__(self,codigo,nombre,precio):
        self.__codigo = codigo
        self.nombre = nombre
        self.precio = precio


    def setCodigo(self,codigo):
        self.__codigo= codigo

    def getCodigo(self):
        #self.__mensaje()
        return self.__codigo

    def __mensaje(self):
        print("Segundo C " + self.__codigo)

    def getData(self):
        return self.__codigo+" "+self.nombre+" "+str(self.precio)+"\n"


class Inventario:

    def __init__(self,codigo,productos,total):
        self.__codigo= codigo
        self.productos = productos
        self.total = total

    def getLista(self):
        cad = ""
        for i in range(len(self.productos)):
            cad = cad + self.productos[i].getData()
        return cad

    def setCodigo(self,codigo):
        self.__codigo= codigo

    def getCodigo(self):
        return self.__codigo

    def getData(self):
        return self.__codigo+"\n"+self.getLista()+"\n"+str(self.total)

class Persona:

    def __init__(self,ruc,nombre,apellido):
        self.__ruc= ruc
        self.nombre=nombre
        self.apellido = apellido

    def setRuc(self,ruc):
        self.__ruc = ruc

    def getRuc(self):
        return self.__ruc

    def getData(self):
        return self.__ruc+" "+self.nombre+" "+self.apellido

    def getFields(self):
        return "Cedula o Ruc:"+self.__ruc+\
               "\nNombre:"+self.nombre+"\nApellido:"+self.apellido

class Cliente(Persona):

    def __init__(self,p1,p2,p3):
        Persona.__init__(self,p1,p2,p3)

class Proveedor(Persona):

    def __init__(self,p1,p2,p3):
        Persona.__init__(self,p1,p2,p3)

class Factura:

    def __init__(self,nfactura,total):
        self.__n_factura= nfactura
        self.total = total

    def setNfactura(self,nfactura):
        self.__n_factura= nfactura

    def getNFactura(self):
        return self.__n_factura

    def getData(self):
        return str(self.__n_factura)+" "+str(self.total)

class FacturaCompra(Factura):

    def __init__(self,p1,p2,p3):
        Factura.__init__(self,p1,p2)
        self.__ruc_proveedor = p3

    def setRucProveedor(self,ruc):
        self.__ruc_proveedor=ruc

    def getRucProveedor(self):
        return self.__ruc_proveedor

    def getData(self):
        return str(self.getNFactura())+" "+\
               str(self.total)+" "+self.__ruc_proveedor

class FacturaVenta(Factura,Operacion):

    def __init__(self,p1,p2,p3):
        Factura.__init__(self,p1,p2)
        self.__ruc_cliente=p3

    def setRucCliente(self,ruc):
        self.__ruc_cliente=ruc

    def getRucCliente(self):
        return self.__ruc_cliente

    def getData(self):
        print(self.saludo("Segundo C"))
        self.presentacion()
        return str(self.getNFactura())+" "\
               +str(self.total)+" "+self.__ruc_cliente




"""
obFV = FacturaVenta(20,700,"0977002")
obFV.setRucCliente("123006")
obFV.setNfactura(34)
obFV.total=900
print(obFV.getData())
obFC = FacturaCompra(13,500,"123001")
print(obFC.getData())
obf = Factura(12,400)
obf.setNfactura(20)
print(obf.getData())
obC = Cliente("12345","CARLOS JULIO","VIVAR PEREZ")
obC.setRuc("098765")
print(obC.getData())

lista = []
obp1= Producto("A001","CAMISA",20)
obp2= Producto("A002","BLUSA",30)
obp3= Producto("A003","PANTALON",32.10)
obp4= Producto("A004","ABRIGO",20.90)
obp5= Producto("A005","ZAPATO",40)
lista.append(obp1)
lista.append(obp2)
lista.append(obp3)
lista.append(obp4)
lista.append(obp5)
oper = Operacion()
codigo = input("Codigo:")
obj = oper.getProduct(codigo,lista)
if obj!= None:
    print(obj.getData())
else:
    print("Codigo no existe!!")
codigo = input("Codigo:")
pos= oper.getProductPos(codigo,lista)
if pos<0:
    print("No existe el codigo")
else:
    print("El elemento esta en la posicion:"+str(pos))
#obI = Inventario("I001",lista,200)
#print(obI.getData())
"""

class Account:

    def __init__(self,url):
        self.__url = url

    def getUrl(self):
        return self.__url

class BlogAcount(Account):

    def __init__(self, entries):
        self.__entries = entries

    def getEntries(self):
        return self.__entries

class WikiAccount(Account):

    def __init__(self,entries):
        self.__entries = entries

    def getEntries(self):
        return self.__entries

class DualPurposeAccount(BlogAcount):

    def __init__(self):
        pass


class Usuario:

    def __init__(self,*param):
        self.usuario=param[0]
        self.password = param[1]
        self.nombre= param[2]
        self.apellido=param[3]
        self.correo=param[4]
        self.profesion=param[5]
        self.estado=param[6]


