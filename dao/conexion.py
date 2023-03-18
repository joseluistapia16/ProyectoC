import mysql.connector as mc
class Conexion:

    def conecta(self,name):
        cone = None
        credencial ={
            'host': 'localhost',
            'port': '3306',
            'user': 'root',
            'password':'1234',
            'database':name
        }
        try:
            cone= mc.connect(**credencial)
        except(mc.errors.ProgrammingError,mc.InterfaceError) as ex:
            print(str(ex))
        return cone

# Codigo de Prueba
#cx = Conexion()
#print(cx.conecta("segundoc27"))