from cProfile import label
from dis import Instruction
from distutils.log import info
from importlib.resources import open_text
from operator import concat
from pickle import FRAME
import plistlib
from tkinter import * 
import tkinter as tk
from tkinter import font
from tkinter import filedialog
from unittest import TextTestResult
from tkinter import messagebox
from tkinter import Entry 
from tkinter import ttk
import sqlite3


def infoadicional():
    messagebox.showinfo("Family Help", "Hecho por Thomas Molina y Erwin Bañol")


def ayuda():
    messagebox.showinfo("Atencion al cliente", "Para brindarle una mejor asesoría comuniquese con el lider del grupo: thomas_molina23212@elpoli.edu.co") 


def ventana1():
    import encuetaalimentos
    encuetaalimentos 
    encuetaalimentos.mainloop()

def ventana2():
    import encuestaspersonas
    encuestaspersonas
    encuestaspersonas.mainloop()

    
def ventana4():
    win4=tk.Toplevel()
    win4.geometry('1000x500')
    win4.configure(background="#2e3192")
    
    scroll=tk.Scrollbar(win4)
    InfoMod1=tk.Text(win4, height=60, width=300)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)
    InfoMod1.pack(side=tk.LEFT, fill=tk.Y)
    scroll.config(command=InfoMod1.yview)
    InfoMod1.config(yscrollcommand=scroll.set)
    Infinal="""
    La aplicación Family Help es una aplicación de escritorio que permite a los usuarios recolectar dos tipos de datos, 
    los alimentos que se van a ingresar y los otros datos que se pueden recolectar en la encuesta que se le hace 
    a las personas, para si hacer dos listas . Donde la persona 
    puede corregir y borrar la lista.
    
    El primer botón es el botón llamado Alimentos, donde se elegirá dos tipos de opciones de alimentos:
    
    -Alimentos no perecederos como atún, frijoles, garbanzos, etc. Por motivos externos al proyecto.
    se tuvo que globalizar todo este tipo de alimentos a un solo nombre.
    
    -Agua o líquidos. Donde estos pueden ser líquidos como agua, gaseosas, jugos en cajas o botellas con largas fechas 
    de vencimiento. 
    
    Cuando se da click en continuar en las dos encuestas la página se reinicia y guarda los datos escritos en 
    dichos campos requeridos., para así volver a digitar dichos campos. No es necesario de pulsar click en continuar 
    dos veces porque así se repetirá la información que se desea guardar. 



    """
    InfoMod1.insert(tk.END, Infinal)
    win4.title("FamilyHelp")
    win4.iconbitmap("FHsimbolo.ico")
    barramenu=Menu(win4)
    win4.config(menu=barramenu, width=300, height=300)
    archivoayuda=Menu(barramenu, tearoff=0)
    archivoayuda.add_command(label="Licencia", command=infoadicional)
    archivoayuda.add_command(label="Acerda de...", command=ayuda)
    barramenu.add_cascade(label="Ayuda", menu=archivoayuda)


if __name__=="__main__":
    raiz=Tk    
    raiz = tk.Tk()
    raiz.geometry()
    raiz.resizable(True, True)
    raiz.title("FamilyHelp")
    raiz.iconbitmap("FHsimbolo.ico")
    raiz.config(bg="#2e3192")

    fhframe = Frame(raiz,width=1000, height=2000)
    fhframe.pack(fill="both", expand=True)
    fhframe.config(bg="#2e3192")
    FHimage = PhotoImage(file="FamilyHelp222.png")
    emptylabel1 = Label(fhframe,bg="#2e3192").pack(pady=1)
    mlabel = Label(fhframe, image = FHimage,bg="#2e3192").pack(pady=2)
    emptylabe2 = Label(fhframe,bg="#2e3192").pack(pady=3)
    tex=Label(fhframe, text="MENÚ",bg="#2e3192", fg="white", font=('Arial', 25, "bold" )).pack(pady=4)
    boton1=tk.Button(fhframe,text="Alimentos",bg="#0071bc", fg="white", command=ventana1,width="20", height="1", font=('Arial', 20, "bold" )).pack(pady=5)
    boton2=tk.Button(fhframe,text=" Encuestas ",bg="#0071bc", fg="white", command=ventana2,width="20", height="1", font=('Arial', 20, "bold" )).pack(pady=6)
    # boton3=tk.Button(fhframe,text=" Listas  ",bg="#0071bc", fg="white", command=ventana3,width="20", height="1", font=('Arial', 20, "bold" )).pack(pady=7)
    boton4=tk.Button(fhframe,text="Informacion",bg="#0071bc", fg="white", command=ventana4,width="20", height="1", font=('Arial', 20, "bold" )).pack(pady=8)


    barramenu=Menu(raiz)
    raiz.config(menu=barramenu, width=300, height=300)
        
    archivoayuda=Menu(barramenu, tearoff=0)
    archivoayuda.add_command(label="Licencia", command=infoadicional)
    archivoayuda.add_command(label="Acerda de...", command=ayuda)
    barramenu.add_cascade(label="Ayuda", menu=archivoayuda)

    alimentosoliquidosa=StringVar()
    aguaoliquidosa=StringVar()
    nombrea=StringVar()
    apellidoa=StringVar()
    edada=StringVar()
    direcciona=StringVar()
    varopcion1a=StringVar()
    varopcion2a=StringVar()
    raiz.mainloop()