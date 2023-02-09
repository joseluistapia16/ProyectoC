from dominio.entidades import *
from procesos.procesos import *
from menuC.menuC import *
from archivos.archivos import *
class Core:

    def __init__(self):
        self.ruta="C:/Users/sopor/PycharmProjects/SegundoC_3/segundoC.csv"
        self.arch = ArchivoC()
        self.lista = self.arch.getAllClients(self.ruta)
        self.men = MenuC()
        self.inp = Input()
        self.oper = Operacion()

    def start(self):
        opc = ("Registro","Consulta","Actualizar",
               "Eliminar","Listar","Salir")
        op = self.men.getMenu(opc)
        if op == 1:
            self.__registro()
            self.start()
        if op==2:
            self.__consulta()
            self.start()
        if op==3:
            self.__actualizar()
            self.start()
        if op==4:
            self.__eliminar()
            self.start()
        if op==5:
            self.__listar()
            self.start()

        if op==6:
            print("Gracias por su visita!!")

    def __registro(self):
        print("\t\tRegistro de Clientes")
        cedula = input("Cedula o Ruc:")
        nombre = input("Nombre:")
        apellido= input("Apellido:")
        obj = Cliente(cedula,nombre,apellido)
        reg = obj.getRuc()+";"+obj.nombre+";"+obj.apellido+";\n"
        self.arch.create(self.ruta,reg,"a")
        print("Datos registrados")
        input("<Enter> para continuar..")

    def __consulta(self):
        print("\t\tConsulta de clientes.")
        ruc = input("Cedula o Ruc:")
        self.lista=self.arch.getAllClients(self.ruta)
        obj = self.oper.getClient(ruc,self.lista)
        if obj!=None:
            print(obj.getFields())
        else:
            print("Cedula o Ruc no existe!")
        input("<Enter> para continuar..")


    def __actualizar(self):
        print("\t\tActualizar datos de clientes.")
        ruc = input("Cedula o Ruc:")
        self.lista= self.arch.getAllClients(self.ruta)
        pos = self.oper.getClientPos(ruc,self.lista)
        if pos>-1:
            print(self.lista[pos].getFields())
            nombre = input("Nombre:")
            apellido = input("Apellidos:")
            self.lista[pos].nombre = nombre
            self.lista[pos].apellido=apellido
            msg = ""
            for i in range(len(self.lista)):
                msg=msg+self.lista[i].getRuc()+";"+self.lista[i].nombre\
                    +";"+self.lista[i].apellido+";\n"
            self.arch.create(self.ruta,msg,"w")
            print("Datos actualizados...")
        else:
            print("Cedula no existe!!")
        input("<Enter> para continuar..")

    def __eliminar(self):
        print("\t\tEliminar datos de clientes.")
        ruc = input("Cedula o Ruc:")
        self.lista= self.arch.getAllClients(self.ruta)
        pos = self.oper.getClientPos(ruc,self.lista)
        if pos>-1:
            print(self.lista[pos].getFields())
            self.lista.pop(pos)
            msg = ""
            for i in range(len(self.lista)):
                msg=msg+self.lista[i].getRuc()+";"+self.lista[i].nombre\
                    +";"+self.lista[i].apellido+";\n"
            self.arch.create(self.ruta,msg,"w")
            print("Datos eliminados!!")
        else:
            print("Cedula no existe!!")
        input("<Enter> para continuar..")



    def __listar(self):
        print("\t\tListado de clientes")
        self.lista=self.arch.getAllClients(self.ruta)
        for i in range(len(self.lista)):
            print(self.lista[i].getData())
        input("<Enter> para continuar..")

