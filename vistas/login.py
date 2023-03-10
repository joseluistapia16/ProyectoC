from tkinter import messagebox
from tkinter import *
from vistas.Registrarse import *
from vistas.gui_process import *
from vistas.menuC import *
class LoginC:
    def __init__(self):
        self.cv= GuiProcess()
        self.getWindow()
        self.getLabels()
        self.getInput()
        self.getButtons()
        self.ven.mainloop()

    def getWindow(self):
        self.ven = Tk()
        self.ven.title("Segundo C")
        self.cv.center(self.ven,400,300)
        #self.ven.geometry("400x300")
        self.ven.config(bg="purple")
        self.ven.resizable(0, 0)

    def getLabels(self):
        lb1 = Label(self.ven, fg="white",
                    font=("Tahoma", 20),
                    text="Usuario", bg="purple").place(x=145, y=50)
        lb2 = Label(self.ven, fg="white",
                    font=("Tahoma", 20),
                    text="Password", bg="purple").place(x=130, y=135)

    def getInput(self):
        self.usuario = Entry(self.ven, font=("Arial", 20),
                             bg="yellow", fg="blue")
        self.usuario.place(x=120, y=100, height=35, width=160)

        self.password = Entry(self.ven, font=("Arial", 20),
                              bg="yellow", fg="blue", show="*")
        self.password.place(x=120, y=175, height=35, width=160)

    def getButtons(self):
        btn1 = Button(self.ven, relief="flat",
                      text="Aceptar", bg="green",
                      font=("Arial", 12),
                      command=self.accion,
                      cursor="hand1").place(x=100, y=240,
                                            width=80)
        btn2 = Button(self.ven, relief="flat",
                      text="Cancelar", bg="green",
                      font=("Arial", 12),
                      command=self.ven.destroy,
                      cursor="hand1").place(x=210, y=240,
                                            width=80)
        btn3 = Button(self.ven, relief="flat",
                      text="Registrarse", bg="green",
                      font=("Arial", 10),
                      command=self.accion1,
                      cursor="hand1").place(x=305, y=10,
                                            width=90, height=20)

    def accion1(self):
        obj1 = Registro()
    def accion(self):
        if self.usuario.get()=="SegundoC" and self.password.get()=="1234":
            obj = Usuario("SegundoC", "1234", "Adrian", "Cevallos",
                          "adrian@gmail.com", "Desarrollador", "A")
            MenuC(obj)
        else:
            messagebox.showinfo("Login",
                                "Credenciales invalidas!",parent=self.ven)




#Codigo de prueba
ob1 = LoginC()