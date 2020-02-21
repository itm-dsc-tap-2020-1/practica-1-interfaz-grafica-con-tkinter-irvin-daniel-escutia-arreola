import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import scrolledtext

def imprime1():
    cad1="Nombre: "+nomb.get()+" "+apat.get()+" "+amat.get()
    cad1+="\nDirección: "+dire.get()+"\nColonia: "+col.get()
    cad1+="\nCiudad: "+cdd.get()+"\nMunicipio: "+mun.get()
    mBox.showinfo("Datos Personales",cad1)

def imprime2():
    cad2="Pasatiempos:\n"
    if(op1.get()==1):
        cad2+="*"+chb1.cget("text")+"\n"
    if(op2.get())==1:
        cad2+="*"+chb2.cget("text")+"\n"
    if(op3.get())==1:
        cad2+="*"+chb3.cget("text")+"\n" 
    cad2+="Estado Civil: "    
    if op0.get()==1:
        cad2+=rad1.cget("text")+"\n"
    elif op0.get()==2:
        cad2+=rad2.cget("text")+"\n"
    else:
        cad2+=rad3.cget("text")+"\n"
    cad2+="Objetivo de la Vida: "+obj.get(1.0,"end-1c")        
    mBox.showinfo("Datos Extras",cad2)       

def valid():
    valid1()
    valid2()

def valid1():
    if nomb.get() and apat.get() and amat.get() and dire.get():
        imprime1()
    else:
        mBox.showinfo("Error","Hay campos vacios en \nDatos Personales")

def valid2():
    if op0.get() and obj.get(1.0,"end-1c")!="":
        imprime2()
    else:
        mBox.showinfo("Error","Hay campos vacios en \nDatos Extras")  

def acerca():
    mBox.showinfo('Acerca de','Irvin Daniel Escutia Arreola \n \t ISC \n        Febrero 2020')

def salir():
    ventana.quit()
    ventana.destroy()
    exit()

ventana=tk.Tk()
ventana.title("Sistema Escolar - Menu")
ventana.tk_setPalette('light gray')
barra_menu= Menu(ventana)
ventana.config(menu=barra_menu)
opcsys= Menu(barra_menu)
opcsys.add_command(label="Imprimir",command=valid)
opcsys.add_command(label="Salir",command=salir)
barra_menu.add_cascade(label="Sistema",menu=opcsys)
opchlp= Menu(barra_menu)
opchlp.add_command(label="Acerca de",command=acerca)
barra_menu.add_cascade(label="Ayuda",menu=opchlp)

tabControl= ttk.Notebook(ventana)
tab1= ttk.Frame(tabControl)
tabControl.add(tab1,text="Datos Personales")
tabControl.pack(expand=1,fill="both")
tab2= ttk.Frame(tabControl)
tabControl.add(tab2,text="Datos Extras")

ttk.Label(tab1,text="Nombre").grid(column=0,row=1)
ttk.Label(tab1,text="Apellido P.").grid(column=0,row=2)
ttk.Label(tab1,text="Apellido M.").grid(column=0,row=3)
ttk.Label(tab1,text="Dirección").grid(column=0,row=4)
ttk.Label(tab1,text="Colonia").grid(column=0,row=5)
ttk.Label(tab1,text="Ciudad").grid(column=0,row=6)
ttk.Label(tab1,text="Municipio").grid(column=0,row=7)

nomb= tk.StringVar()
apat= tk.StringVar()
amat= tk.StringVar()
dire= tk.StringVar()
col=tk.StringVar()
cdd=tk.StringVar()
mun=tk.StringVar()

ttk.Entry(tab1, width=20,textvariable=nomb).grid(column=1,row=1)
ttk.Entry(tab1, width=20,textvariable=apat).grid(column=1,row=2)
ttk.Entry(tab1, width=20,textvariable=amat).grid(column=1,row=3)
ttk.Entry(tab1, width=20,textvariable=dire).grid(column=1,row=4)
cols= ttk.Combobox(tab1, width=15, textvariable=col,state="readonly")
cdds= ttk.Combobox(tab1, width=15, textvariable=cdd,state="readonly")
muns= ttk.Combobox(tab1, width=15, textvariable=mun,state="readonly")

cols.grid(column=1,row=5)
cdds.grid(column=1,row=6)
muns.grid(column=1,row=7)

cols['values']= ("Centro","Fuentes","Colinas")
cols.current(0)
cdds['values']= ("Morelia","Zimpanio","Atecuaro")
cdds.current(0)
muns['values']= ("Michoacán","Lazaro","Uruapan")
muns.current(0)

warn1= ttk.Label(tab1,text="Falta llenar campos")
warn2= ttk.Label(tab2,text="Falta llenar campos")
bot1= ttk.Button(tab1, text="Imprimir Datos Personales", command=valid1)
bot1.grid(column=10,row=7)

ttk.Label(tab2,text="Pasatiempos").grid(column=0,row=1)
ttk.Label(tab2,text="Estado Civil").grid(column=0,row=3)
ttk.Label(tab2,text="Objetivo de la Vida").grid(column=0,row=5)

op1= tk.IntVar()
op2= tk.IntVar()
op3= tk.IntVar()
op0= tk.IntVar()

obj= scrolledtext.ScrolledText(tab2,width=30,height=3,wrap=tk.WORD)
obj.insert(1.0,"")
obj.grid(column=0,row=8)
bot2= ttk.Button(tab2,text="Imprimir Datos",command=valid2)
bot2.grid(column=3,row=8)

chb1= ttk.Checkbutton(tab2,text="Leer",variable=op1)
chb1.grid(column=0,row=2,sticky=tk.W)
chb2= ttk.Checkbutton(tab2,text="Películas",variable=op2)
chb2.grid(column=1,row=2,sticky=tk.W)
chb3= ttk.Checkbutton(tab2,text="Redes Sociales",variable=op3)
chb3.grid(column=4,row=2,sticky=tk.W)

rad1= ttk.Radiobutton(tab2,text="Soltero",variable=op0,value=1)
rad1.grid(column=0,row=4, sticky=tk.W)
rad2= ttk.Radiobutton(tab2,text="Casado",variable=op0,value=2)
rad2.grid(column=1,row=4, sticky=tk.W)
rad3= ttk.Radiobutton(tab2,text="Viudo",variable=op0,value=3)
rad3.grid(column=4,row=4, sticky=tk.W)

ventana.mainloop()