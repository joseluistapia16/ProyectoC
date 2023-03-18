import mysql.connector as mc
from dao.conexion import *
from dominio.entidades import *
class CrudUsuario:

   def __init__(self):
      self.cone = Conexion()

   def insertUser(self,base,datos):
      msg = ""
      try:
         con = self.cone.conecta(base)
         cursor1= con.cursor()
         sql ="insert into usuario(usuario,password,nombres,apellidos," \
              "correo,profesion,estado) values" \
              "(%s,%s,%s,%s,%s,%s,%s)"
         cursor1.execute(sql,datos)
         con.commit()
         con.close()
         msg = "Registro grabado con exito!"
      except(mc.errors.InterfaceError) as ex:
         msg = str(ex)
      return msg

   def getUser(self,base,datos):
       obj = None
       con = self.cone.conecta(base)
       cursor1 = con.cursor()
       sql = "select * from usuario where usuario=%s"
       cursor1.execute(sql,datos)
       result = cursor1.fetchall()
       con.close()
       if len(result)>0:
           obj = Usuario(result[0][0],
                result[0][1],result[0][2],
                result[0][3],result[0][4],
                result[0][5],result[0][6])
       return obj


#Codigo de prueba
cr = CrudUsuario()
""" 
12345","JIMMY ALEJANDRO",
         "BELTRAN TIGUA","beltran@gmail.com",
         "Desarrollador","A")
"""
#print(cr.insertUser("segundoc2",datos))
datos = ("beltra237",)
obj = cr.getUser("segundoc2",datos)
if obj!=None:
    print(obj.usuario,obj.nombre,obj.apellido)
else:
    print("Usuario no existe!")


