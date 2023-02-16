from tkinter import *
from dominio.entidades import *
from vistas.newStudent import *
from vistas.gui_process import *
class MenuC:

    def __init__(self,obj=None):
        self.cv= GuiProcess()
        titulo =""
        if obj!=None:
            titulo="Usuario: "+obj.nombre+" "+obj.apellido+" ."
        self.__getWindow(titulo)
        self.__getMenu()
        self.ven.mainloop()

    def __getWindow(self,titulo=None):
        self.ven = Tk()
        self.ven.title(titulo)
        self.cv.center(self.ven,1100,570)
        self.ven.config(bg="purple")
        self.ven.resizable(0, 0)

    def __getMenu(self):
        self.menu = Menu(self.ven)
        self.ven.config(menu=self.menu)
        #Cascada 1
        item1 = Menu(self.menu)
        self.menu.add_cascade(label="Archivo",menu=item1)
        item1.add_command(label="Registro", command=self.opc1)
        item1.add_command(label="Gestion de estudiantes")
        item1.add_separator()
        item1.add_command(label="Salir",command=self.__salir)
        #Cascada 2
        item2 = Menu(self.menu)
        self.menu.add_cascade(label="About",menu=item2)
        item2.add_command(label="About")

    def __salir(self):
        self.ven.destroy()

    def opc1(self):
        NewStudent()


# Codigo de prueba
#men = MenuC()
