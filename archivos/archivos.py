from dominio.entidades import *

class ArchivoC:

    def create(self,ruta,registro,modo):
        arch = open(ruta,modo)
        arch.write(registro)
        arch.close()

    def getAllClients(self,ruta):
        lista = []
        try:
            arch = open(ruta,"r")
            for linea in arch.readlines():
                tupla = linea.split(";")
                obj = Cliente(tupla[0],tupla[1],tupla[2])
                lista.append(obj)
        except:
            print("....")
        return lista