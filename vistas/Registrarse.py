from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from vistas.gui_process import *
from dominio.entidades import *
class Registro:
    def __init__(self):
        self.cv= GuiProcess()
        self.lista = ["Desarrollador","Analista","Administrativo",
                      "Lider de proyecto"]
        self.getWindow()
        self.getLabels()
        self.getInputs()
        self.getButtons()
        self.ven.mainloop()

    def getWindow(self):
        self.ven = Toplevel()
        self.ven.title("Registro de usuario")
        self.cv.center(self.ven,700,490)
        self.ven.config(bg="purple")
        self.ven.resizable(0, 0)

    def getLabels(self):
        posX=120
        lb1 = Label(self.ven, fg="white",
                    font=("Tahoma", 20),
                    text="Registro de usuario", bg="purple").place(x=220, y=30)
        lb2 = Label(self.ven, fg="white",
                    font=("Tahoma", 20),
                    text="Usuario", bg="purple").place(x=posX, y=100)
        lb3 = Label(self.ven, fg="white",
                    font=("Tahoma", 20),
                    text="Password", bg="purple").place(x=posX, y=150)
        lb4 = Label(self.ven, fg="white",
                    font=("Tahoma", 20),
                    text="Nombres", bg="purple").place(x=posX, y=200)
        lb5 = Label(self.ven, fg="white",
                    font=("Tahoma", 20),
                    text="Apellidos", bg="purple").place(x=posX, y=250)
        lb6 = Label(self.ven, fg="white",
                    font=("Tahoma", 20),
                    text="Correos", bg="purple").place(x=posX, y=300)
        lb7 = Label(self.ven, fg="white",
                    font=("Tahoma", 20),
                    text="Profesion", bg="purple").place(x=posX, y=350)

    def getInputs(self):
        posX=350
        self.usuario = Entry(self.ven, font=("Arial", 15),
                             bg="white", fg="blue")
        self.usuario.place(x=posX, y=108, height=25, width=200)
        self.password = Entry(self.ven, font=("Arial", 15),
                              bg="white", fg="blue", show="*")
        self.password.place(x=posX, y=158, height=25, width=200)
        self.nombre = Entry(self.ven, font=("Arial", 15),
                             bg="white", fg="blue")
        self.nombre.place(x=posX, y=208, height=25, width=200)
        self.apellido = Entry(self.ven, font=("Arial", 15),
                             bg="white", fg="blue")
        self.apellido.place(x=posX, y=258, height=25, width=200)
        self.correo = Entry(self.ven, font=("Arial", 15),
                             bg="white", fg="blue")
        self.correo.place(x=posX, y=308, height=25, width=200)
        self.profesion = Combobox(self.ven,state="readonly", font=("Tahoma",15),
                                  values=self.lista)
        self.profesion.place(x=posX,y=358,width=200,height=30)

    def getButtons(self):
        btn1 = Button(self.ven, relief="flat",
                      text="Nuevo", bg="green",
                      font=("Arial", 11),
                      command=self.vaciar,
                      cursor="hand1").place(x=570, y=30,
                                            width=110,height=25)
        btn2 = Button(self.ven, relief="flat",
                      text="Guardar", bg="green",
                      font=("Arial", 12),
                     #command=self.ven.destroy,
                      cursor="hand1").place(x=200, y=420,
                                            width=110,height=40)
        btn3 = Button(self.ven, relief="flat",
                      text="Cancelar", bg="green",
                      font=("Arial", 12),
                      command=self.ven.destroy,
                      cursor="hand1").place(x=360, y=420,
                                            width=110, height=40)

    def accion(self):
        messagebox.showinfo("Advertencia", self.usuario.get(),
                            parent=self.ven)

    def vaciar(self):
        self.usuario.delete(0,END)
        self.password.delete(0,END)
        self.nombre.delete(0,END)
        self.apellido.delete(0,END)
        self.correo.delete(0,END)

# Codigo de prueba
#obj = Registro()