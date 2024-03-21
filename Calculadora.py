import tkinter
    #Jonathan Lancheros
    #Jonathan Arevalo
    #Cristian Rodrguez
ventana = tkinter.Tk() #Contenedor de elementos graficos 
ventana.geometry("500x500")

cajaNumero1 = tkinter.Entry(ventana, font="Helveltica 20") 
cajaNumero1.pack()
cajaNumero2 = tkinter.Entry(ventana, font="Helveltica 20") 
cajaNumero2.pack()


def multiplicar():
    numero1 = int(cajaNumero1.get())
    numero2 = int(cajaNumero2.get())
    resulMultiplicacion = numero1 * numero2
    etiquetaResul["text"] = resulMultiplicacion
  
def sumar():
    numero1 = int(cajaNumero1.get())
    numero2 = int(cajaNumero2.get())
    resulSumar = numero1 + numero2
    etiquetaResul["text"] = resulSumar

def restar():
    numero1 = int(cajaNumero1.get())
    numero2 = int(cajaNumero2.get())
    resulrestar = numero1 - numero2
    etiquetaResul["text"] = resulrestar
  
def dividir():
    numero1 = int(cajaNumero1.get())
    numero2 = int(cajaNumero2.get())
    if numero2 != 0:
        resuldividir = numero1 / numero2
        etiquetaResul["text"] = resuldividir

    else:
        etiquetaResul1 = tkinter.Label(ventana,text="no se puede dividir en cero", bg="gray", font="Helveltica 15") 
        etiquetaResul1.pack()

   
  
def saludo(num1, num2):
    print(num1*num2)

boton = tkinter.Button(ventana,text="sumar", command= sumar)
boton.place(x=80,y=200)
boton = tkinter.Button(ventana,text="restar", command= restar)
boton.place(x=180,y=200)
boton = tkinter.Button(ventana,text="multiplicar", command= multiplicar)
boton.place(x=260,y=200)
boton = tkinter.Button(ventana,text="dividir", command= dividir)
boton.place(x=380,y=200)



etiquetaResul = tkinter.Label(ventana,text="", bg="gray", font="Helveltica 15") 
etiquetaResul.pack()

ventana.mainloop()

