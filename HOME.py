#Importamos la librería tkinter para crear una ventana
import tkinter



#Se crea la ventana principal con el método Tk() y se guarda en la variable ventana
ventana = tkinter.Tk()

#Se le da un título a la ventana con el método title()
ventana.title("Dominos Pizza")

#Se le da un tamaño a la ventana con el método geometry()
ventana.geometry("800x500")

#Se le coloca un icono a la ventana con el método iconbitmap()
ventana.iconbitmap("dominos.ico")#El icono debe estar en formato .ico

#Se coloca un color de fondo a la ventana con el método configure()
ventana.configure(background="white") #Los colores se colocan en inglés

#Se coloca una imagen en la ventana con el método PhotoImage()
imagen = tkinter.PhotoImage(file="dominos.png")

#Se modifica el tamaño de la imagen con el método subsample()
imagen = imagen.subsample(1, 1)#El primer valor es el ancho y el segundo el alto de la imagen en pixeles

#Se coloca la imagen en la ventana con el método Label()
label = tkinter.Label(ventana, image=imagen).pack(side="left")

#Con el comando def se crea una función con el nombre de botones
def accion_btn():
    #Se crea varios botones con el método Button() y se guarda en la variable boton
    print("Hola Mundo") 

#Se crea una función para configurar los botones
def conf_btn(ventana, texto, accion_btn, ancho, wrplen): 
    #Se le crean los parámetros a la función (los parametros son variables que se le pasan a la función, es decir, valores que podemos cambiar de forma manual)
    boton = tkinter.Button(
        ventana, #Primeramente debemos colocar la ventana donde se colocará el botón
        text=texto, #Text es el texto que se mostrará en el botón, texto es un parametro que se podrá cambiar
        command=accion_btn, #Command es la acción que realizará el botón, accion_btn ya está creada, por lo que imprimirá "Hola Mundo" al presionar el botón en la consola
        relief="flat", #Relief es el tipo de borde que tendrá el botón, flat es un borde plano, más información: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/relief.html
        fg="white", #Fg es el color del texto del botón, white es blanco, tamnién los colores pueden ser hexadecimales, más información: https://www.w3schools.com/colors/colors_picker.asp
        bg="#006491", #Bg es el color de fondo del botón, #006491 es un color azul, también los colores pueden ser hexadecimales
        font=("Arial", 12), #Font es la fuente del texto del botón, Arial es la fuente y 12 es el tamaño de la fuente, más información: https://www.w3schools.com/cssref/css_websafe_fonts.asp
        width=ancho, #Width es el ancho del botón, ancho es un parametro que se podrá cambiar
        height=2, #Height es el alto del botón, 2 es el alto del botón
        padx=10, #Padx es el espacio que habrá entre el texto y el borde del botón de manera horizontal, 10 es el espacio
        pady=10, #Pady es el espacio que habrá entre el texto y el borde del botón de manera vertical, 10 es el espacio
        cursor="hand2", #Cursor es el tipo de cursor que se mostrará al pasar el mouse por el botón, hand2 es una manito, más información: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/cursors.html
        activebackground="white", #Activebackground es el color de fondo del botón al presionarlo, white es blanco
        activeforeground="#006491", #Activeforeground es el color del texto del botón al presionarlo, #006491 es un color azul
        bd=0, #Bd es el grosor del borde del botón, 0 es el grosor
        justify="center", #Justify es la posición del texto del botón, center es centrado, más información: https://www.tutorialspoint.com/how-to-justify-text-in-label-in-tkinter-in-python-need-justify-in-tkinter
        anchor="center", #Anchor es la posición del texto dentro del botón, center es centrado, más información: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/anchors.html
        wraplength=wrplen, #Wraplength es el ancho del botón, wrplen es un parametro que se podrá cambiar
        state="normal", #State es el estado del botón, normal es normal, más información: https://www.geeksforgeeks.org/how-to-change-tkinter-button-state/
        overrelief="ridge", #Overrelief es el tipo de borde que tendrá el botón al pasar el mouse por el botón, flat es un borde plano, más información: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/relief.html
        repeatdelay=1000, #Repeatdelay es el tiempo que tardará el botón en repetir la acción, 1000 es 1 segundo
        repeatinterval=100 #Repeatinterval es el tiempo que tardará el botón en repetir la acción, 100 es 0.1 segundo
    )
    boton.pack()
    return boton

#Se procede a crear un boton con el método Button() y se guarda en la variable boton
# Crear botones utilizando la función crear_boton y configurarlos con la función conf_btn
#La estructura de la función conf_btn es la siguiente: conf_btn(ventana, texto, accion_btn, ancho, wrplen)
boton1 = conf_btn(ventana, "Ordena Online", accion_btn, 8, 80)
boton2 = conf_btn(ventana, "Menú", accion_btn, 8, 80)
boton3 = conf_btn(ventana, "Cupones", accion_btn, 8, 80)
boton4 = conf_btn(ventana, "Rastrea", accion_btn, 8, 80)
boton5 = conf_btn(ventana, "Busca tu tienda más cercana", accion_btn, 15, 150)
boton6 = conf_btn(ventana, "Iniciar Sesión", accion_btn, 8, 80)
boton7 = conf_btn(ventana, "Carrito", accion_btn, 8, 80)

#Se coloca el botón de manera horizontal con el método pack(side="left")
boton1.pack(side="left")
boton2.pack(side="left")
boton3.pack(side="left")
boton4.pack(side="left")
boton5.pack(side="left")
boton6.pack(side="left")
boton7.pack(side="left")

#Se coloca el boton en la ventana con el método pack()
boton1.pack()
boton2.pack()
boton3.pack()
boton4.pack()
boton5.pack()
boton6.pack()
boton7.pack()

#Agrega un espacio entre el botón y el borde de la ventana
ventana.pack_propagate(False)

#Abrimos la ventana con el método mainloop()
ventana.mainloop()


