from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import *
#from vistas.processGui import *
class EditStudent:

    def __init__(self,obj=None):
        #self.cv= GuiProcess()
        self.lista=["DESARROLLO DE SOFTWARE","DISEÑO GRAFICO","MARKETTING"]
        self.__getWindow()
        self.__getFrame()
        self.__getLabels()
        self.__getInputs()
        self.__getButtons()
        self.__fillFields(obj)
        self.ven2.mainloop()

    def __getWindow(self,titulo=None):
        self.ven2 = Toplevel()
        self.ven2.title(titulo)
        self.ven2.geometry("700x490")
        #self.cv.center(self.ven2,700,490)
        self.ven2.config(bg="purple")
        self.ven2.resizable(0,0)

    def __getLabels(self):
        posX = 120
        lb1 = Label(self.marco, bg="purple", fg="white",
                    text="Registro de Estudiantes", font=("Arial", 18)).place(
            x=220, y=20)
        lb2 = Label(self.marco, bg="purple", fg="white",
                    text="Cedula", font=("Arial", 18)).place(
            x=posX, y=100)
        lb3 = Label(self.marco, bg="purple", fg="white",
                    text="Nombres", font=("Arial", 18)).place(
            x=posX, y=150)
        lb4 = Label(self.marco, bg="purple", fg="white",
                    text="Apellidos", font=("Arial", 18)).place(
            x=posX, y=200)
        lb5 = Label(self.marco, bg="purple", fg="white",
                    text="Codigo matricula", font=("Arial", 18)).place(
            x=posX, y=250)
        lb6 = Label(self.marco, bg="purple", fg="white",
                    text="Correo", font=("Arial", 18)).place(
            x=posX, y=300)
        lb7 = Label(self.marco, bg="purple", fg="white",
                    text="Carrera", font=("Arial", 18)).place(
            x=posX, y=350)

    def __getInputs(self):
        posX= 350
        self.cedula = Entry(self.marco,font=("Tahoma",16),bg="#D6EAF8")
        self.cedula.place(x=posX,y=100,width=200,height=25)
        self.nombres = Entry(self.marco,font=("Tahoma",16),bg="#D6EAF8")
        self.nombres.place(x=posX,y=150,width=200,height=25)
        self.apellidos= Entry(self.marco,font=("Tahoma",16),bg="#D6EAF8")
        self.apellidos.place(x=posX,y=200,width=200,height=25)
        self.codigo_mat = Entry(self.marco,font=("Tahoma",16),bg="#D6EAF8")
        self.codigo_mat.place(x=posX,y=250,width=200,height=25)
        self.correo = Entry(self.marco,font=("Tahoma",16),bg="#D6EAF8")
        self.correo.place(x=posX,y=300,width=200,height=25)
        self.carrera= Combobox(self.marco,state="readonly",values=self.lista)
        self.carrera.place(x=posX,y=350,width=200,height=30)

    def __getButtons(self):
        btn1 = Button(self.marco, relief="flat",
                      text="Nuevo", bg ="green",
                      font=("Arial",11),fg="white", cursor="hand1",
                      command=self.__deleteFields
                      ).place(x=570,y=30,width=110,height=25)
        self.guardar= Button(self.marco,relief="flat",text="Guardar",
                             bg="green",font=("Arial",16),fg="white",
                             cursor="hand1",command=self.save)
        self.guardar.place(x=200,y=410,width=110,height=40)
        self.cancelar= Button(self.marco,relief="flat",text="Cancelar",
                             bg="green",font=("Arial",16),fg="white",
                             cursor="hand1",command=self.ven2.destroy)
        self.cancelar.place(x=360,y=410,width=110,height=40)

    def __getFrame(self):
        self.marco = Frame(self.ven2,bd=7, bg="purple")
        self.marco.pack(fill="both",expand=1)
        self.marco.config(cursor="pirate")
        self.marco.config(relief="groove")

    def __deleteFields(self):
        self.cedula.delete(0,END)
        self.nombres.delete(0,END)
        self.apellidos.delete(0,END)
        self.correo.delete(0,END)
        self.codigo_mat.delete(0,END)

    def __fillFields(self,obj):
        self.cedula.insert(0,obj.cedula)
        self.nombres.insert(0,obj.nombres)
        self.apellidos.insert(0,obj.apellidos)
        self.correo.insert(0,obj.correo)
        self.codigo_mat.insert(0,str(obj.cod_mat))

    def save(self):
        pass

