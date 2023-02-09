#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 16:22:41 2021

@author: cerivera
"""

#Código para la interfaz
#Hola no se si eres Armando o Elorduy, pero hice este archivo de manera que se pueda entender
#Para que así te haya podido ayudar en la interfaz, asegurate que quede bonita :)
#Si tienes duda o algo crashea avisame o trata de arreglarlo tu, suerte, ojala te ayuden mis comentarios y mi codigo

#Si tu eres el que esta haciendo la interfaz pon un label donde pueda tener un textvariable que
#se pueda establecer que si no hay ningun producto o la categoria que busca no la tenemos
#Un label que solo se active si no hay coincidencias a ese label llamalo notinstock
#ejemplo: input_user = tkinter.Entry(root, textvariable=user)
#         input_user.pack(padx=20, pady=7)

#en este caso tu textvariable es user, en tu caso deberíua ser notinstock

#de la misma manera tienes que hacer eso con otra variable, en el codigo la encuentras como contact.get()
#y esa variable es la que el usuario ingresa su busqueda, el ejemplo anterior igual te sirve

#Esto es para que puedas poner el scrolled text
import tkinter as tk
from tkinter import ttk
import pyrebase
from datetime import datetime
from clases_proyecto_final import VigenereCipher


root = tk.Tk()
Entrada= tk.StringVar()
notinstock= tk.StringVar()
root.geometry('600x600')
root.title("Farmalisto México")
root.config(cursor="pirate")
dt = datetime.now()
x = ("{}:{}:{}".format(dt.hour, dt.minute, dt.second))
y = ("{}/{}/{}".format(dt.day, dt.month, dt.year))

Titulo = tk.Label(root, text="Farmalisto",fg="white", bg="black",font=("Verdana",20))
Titulo.pack()
hora = tk.Label(root, text= x)
hora.pack()
hora.config(bg="white",fg="black",anchor="nw",font=("Verdana",8))
hora = tk.Label(root, text=y)

hora.pack()
hora.config(bg="white",fg="black",anchor="nw",font=("Verdana",8))


def onConfigure(e):
    my_canvas.configure(scrollregion= my_canvas.bbox('all'))

#esto va despues de tu root y sus configuraciones, y va antes de labels y botones
main_frame = tk.Frame(root)
main_frame.pack(fill= 'both', expand= True )

frame1 = tk.Frame()
frame1.pack(fill='x', expand=True,side="top")

my_canvas = tk.Canvas(main_frame)
my_canvas.pack(side= 'left', fill= 'both', expand= True)

#esto va donde sea dentro de la organización de la interfaz

text_area = tk.Scrollbar(root, orient= 'vertical',  command= my_canvas.yview)
text_area.pack(side= 'right', fill= 'y')

my_canvas.configure(yscrollcommand= text_area.set)
my_canvas.bind('<Configure>', onConfigure)

second_frame= tk.Frame(my_canvas)

my_canvas.create_window((0,0), window= second_frame, anchor= 'nw')

# Esto es para que puedas usar la base de datos

firebaseConfig = {
    'apiKey': "AIzaSyD-WOm4vD6dNTu83S3RScLvpyT7jLg5JiM",
    'authDomain': "catalogfarmacia.firebaseapp.com",
    'projectId': "catalogfarmacia",
    'storageBucket': "catalogfarmacia.appspot.com",
    'messagingSenderId': "652024355594",
    'appId': "1:652024355594:web:b479f41bfe11a3ccbbb8f3",
    'databaseURL': "https://catalogfarmacia-default-rtdb.firebaseio.com/"
  }

firebase = pyrebase.initialize_app(firebaseConfig)

database = firebase.database()





#Esta función es para obtener todos los datos de la base de datos
def onGetdata():
    _users = database.child('Farma Listo').get()
    _response= []
    for user in _users.each():
        _response.append(user.val())

    return _response



#Si quieres ver si funciono esa función prueba:

#Label2 = tk.Label(frame1, text=onGetdata())
#Label2.pack()



#Esta función hace una desencriptación de todos los productos, ya que son los únicos encriptados




def desencriptacion_todo():

    x = onGetdata()
    var1= 'categoria'

    var2= 'producto'

    var3= 'precio'

    key = "hola"

    for i in x:

        product_cod = i[var2]
        plaintext = product_cod
        decoding = VigenereCipher(key)
        product_ready= str(decoding.onDecrypt(product_cod))
        i[var2]= product_ready



    return x

desencriptacion_todo()

Entrada1 = tk.Entry(root, justify="center",textvariable=Entrada).pack()



#### Desencriptacion por categoria para arrojar todo lo que coincida con la categoria buscada
def leer_categorias():

    x = desencriptacion_todo()
    var1= 'categoria'

    var2= 'producto'

    var3= 'precio'

    key = "hola"
    array= []
    #Antes del .get pones como se llama el label donde el usuario pone su busqueda
    lect_usuario = str(Entrada.get())
    for i in x:
        if i.get(var1) == lect_usuario:
            array.append(i)

    return array






#print(leer_categorias())


#Si quieres ver los productos desencriptados prueba:
#print(desencriptacionporcategoria())
#print(leer_categorias())


#Esta función se la pones a un label con un nombre que se entienda que te da todos los productos de esa categoría
def list_label():
    ttk.Label(second_frame, text= '', padding= (10,10)).pack()
    x = leer_categorias()

    if x == "":
        label1["text"]= 'Que raro no tenemos lo que buscas :('
    else:
        for i in x:
            for k,v in i.items():
                ttk.Label(second_frame, text= f'{k}: {v}',  foreground= 'blue', padding= (10,10)).pack()


label1= tk.Label(root).pack()

b2 = tk.Button(root, text="Busqueda por categoría",command= list_label).pack()

#######
#Estas funciones son para la busqueda de productos

#Esta funcion te da todos los productos que coincidan con el producto que el user buscó
def leer_productos():
    x= desencriptacion_todo()

    var1= 'categoria'

    var2= 'producto'

    var3= 'precio'

    key = "hola"

    array = []

    #En esta parte pones (antes del get) como se llama la variable donde el usuario pone su busqueda
    lect_usuario= str(Entrada.get())

    for i in x:

       if lect_usuario in i.get(var2) :
           product_ready= i[var2]

           array.append(product_ready)


    return array







#Esta funcion va a buscar el precio de todos los productos que conseguiste en la anterior función
def precioporproducto():
    productos = leer_productos()

    x= desencriptacion_todo()

    var1= 'categoria'

    var2= 'producto'

    var3= 'precio'

    key = "hola"


    array = []

    for i in x:
        for j in productos:
            if i.get(var2) == j:
                precio= i[var3]
                array.append(precio)


    return array







#Pone en el scrolled text todos los productos que coinciden con el producto buscado con su precio
def read_label():
    ttk.Label(second_frame, text= '', padding= (10,10)).pack()
    x= leer_productos()

    y= precioporproducto()
    if x== "":
        label1["text"]= 'Que raro nada coincide con tu busqueda :('
    else:
        for i, producto in enumerate(x):
            ttk.Label(second_frame, text= f'{producto}:{y[i]}',  foreground= 'blue', padding= (10,10)).pack()

b1 = tk.Button(root, text="Buscar por productos",command= read_label).pack()

Label2 = tk.Label(root, text="Después de una busqueda haga scroll y busque un espacio en blanco", bg="White")
Label2.pack()

root.mainloop()
