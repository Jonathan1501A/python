import tkinter

ventana = tkinter.Tk() #Contenedor de elementos graficos 
ventana.geometry("500x500")


etiqueta = tkinter.Label(ventana,text="Hola mundo", bg="blue") # Colocar un cuadro de color 
etiqueta.pack( fill=tkinter.X )#Coloca el label en pantalla, el Bottom mostrar abajo de la pantalla, Rigth pa mostrar a una lado

cajaNumero1 = tkinter.Entry(ventana, font="Helveltica 20") 
cajaNumero1.pack()
cajaNumero2 = tkinter.Entry(ventana, font="Helveltica 20") 
cajaNumero2.pack()


def numerosDeLaCaja():
    numero1 = int(cajaNumero1.get())
    numero2 = int(cajaNumero2.get())
    resulMultiplicacion = numero1 * numero2
    etiquetaResul["text"] = resulMultiplicacion
    #print("El resultado de la multipliacion es:", resulMultiplicacion)

def saludo(num1, num2):
    print("Hola prgramadores ")
    print(num1*num2)

boton = tkinter.Button(ventana,text="Multiplicar", command= numerosDeLaCaja)
boton.pack()

etiquetaResul = tkinter.Label(ventana,text="", bg="gray", font="Helveltica 15") 
etiquetaResul.pack( fill=tkinter.X )

ventana.mainloop()

