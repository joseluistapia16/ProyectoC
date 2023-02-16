from tkinter import *

class GuiProcess:

    def center(self,objV,ancho,alto):
        y_alto =alto
        x_ancho= ancho
        screen_x= objV.winfo_screenwidth()
        screen_y= objV.winfo_screenheight()
        x_coord = int((screen_x/2)-(x_ancho/2))
        y_coord = int((screen_y/2)-(y_alto/2))
        objV.geometry("{}x{}+{}+{}".format(x_ancho,y_alto,x_coord,y_coord))