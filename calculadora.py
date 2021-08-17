from tkinter import *
from tkinter import ttk

def pulsar(num):
	# global displayText
	displayText.set(displayText.get()+ num)

def evaluar():
	# global displayText
	displayText.set(eval(displayText.get()))


root = Tk()
styleTtk = ttk.Style()
styleTtk.configure("TEntry",
					foreground="red")


root.config(bg= "#282923")
root.title("calculadora")
# root.geometry('300x350')
root.resizable(False, False)

displayText = StringVar()
display = ttk.Entry(root, textvariable=displayText,
					style="TEntry")
display.config(justify="right")
display.grid(row=0,
			 column=0,
			 columnspan=3,
			 padx=10,
			 pady=10)


res=StringVar()


btconfig = {}

boton7 = ttk.Button(root, text ="7", command= lambda: pulsar("7"))
boton7.grid(row=2 ,column=0 )
boton8 = ttk.Button(root, text ="8", command= lambda: pulsar("8"))
boton8.grid(row=2 ,column=1 )
boton9 = ttk.Button(root, text ="9", command= lambda: pulsar("9"))
boton9.grid(row=2 ,column=2 )
botonSuma= ttk.Button(root, text ="+", command= lambda: pulsar("+"))
botonSuma.grid(row=2 ,column=3)

boton4 = ttk.Button(root, text = "4", command= lambda: pulsar("4"))
boton4.grid(row=3 ,column=0 )
boton5 = ttk.Button(root, text = "5", command= lambda: pulsar("5"))
boton5.grid(row=3 ,column=1 )
boton6 = ttk.Button(root, text = "6", command= lambda: pulsar("6"))
boton6.grid(row=3 ,column=2 )

boton1 =ttk.Button(root, text ="1", command= lambda: pulsar("1"))
boton1.grid(row=4 , column=0 )
boton2 =ttk.Button(root, text ="2", command= lambda: pulsar("2"))
boton2.grid(row=4 , column=1 )
boton3 =ttk.Button(root, text ="3", command= lambda: pulsar("3"))
boton3.grid(row=4 , column=2 )

boton = ttk.Button(root, text ="0", command= lambda: pulsar("0"))
boton.grid(row=5, column=0, columnspan =2 )
boton = ttk.Button(root, text =",", command= lambda: pulsar(","))
boton.grid(row=5, column=2 )
botonIgual = ttk.Button(root, text ="=", command= lambda: evaluar())
botonIgual.grid(row=4 ,column=3)

root.mainloop()

#pd: te amo
