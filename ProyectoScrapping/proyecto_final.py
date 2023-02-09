r#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 07:46:11 2021

@author: cerivera
"""
import pyrebase
import requests
from bs4 import BeautifulSoup
from clases_chat import VigenereCipher


key= 'hola'
coding= VigenereCipher(key)

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


#Empieza la parte de mandar los medicamentos con su precio, encriptados


url = "https://www.farmalisto.com.mx/2046-medicamentos"
response= requests.get(url)

#print(response.status_code)

soup= BeautifulSoup(response.text, 'html.parser')


medicamentos= soup.find(id= "js-product-list").find_all('article')
#print(medicamentos_precio)

dict_med= {}



lista_nombres= []
lista_precio= []


for i,c in enumerate(medicamentos):

    h2s= c.find_all('h2')

    for j, k in enumerate(h2s):
        final_name= k.getText().rstrip("\n").replace(',','').replace('+','')

        lista_nombres.append(final_name)


for i, a in enumerate(medicamentos):
    spans= a.find_all('span')

    for j, b in enumerate(spans):
        final_prize= b.getText().rstrip("\n").replace(',','').replace('+','')
        for i in final_prize:
            if i == '$':
                lista_precio.append(final_prize)
            else:
                ''




for i in (lista_nombres):
    if i == '':
        lista_nombres.remove(i)









def cleaning_list(lista, x):
    final_lista= []
    for i in lista:
        y= i.replace(x, '')
        final_lista.append(y)

    return final_lista


lista_nombres= cleaning_list(lista_nombres, '\n')
lista_precio= cleaning_list(lista_precio, '\n')

for i in range(51):
    precio= lista_precio[i]
    nombre= lista_nombres[i]
    dict_med['categoria']= ('medicamentos')
    dict_med['producto']= coding.onEncrypt(nombre)
    dict_med['precio']= precio

    database.child('Farma Listo').push(dict_med)



####################################



#Termina la parte de medicamentos y empieza la parte de vitaminas



url= "https://www.farmalisto.com.mx/2107-suplementos-vitaminas-complementos"

response= requests.get(url)

soup= BeautifulSoup(response.text, 'html.parser')

vitaminas= soup.find(id= "js-product-list").find_all('article')

dict_vit= {}

lista_nombres2= []

lista_precio2= []


for i,c in enumerate(vitaminas):

    h2s= c.find_all('h2')

    for j, k in enumerate(h2s):
        final_name= k.getText().rstrip("\n").replace(',','').replace('+','')

        lista_nombres2.append(final_name)


for i, a in enumerate(vitaminas):
    spans= a.find_all('span')

    for j, b in enumerate(spans):
        final_prize= b.getText().rstrip("\n").replace(',','').replace('+','')
        for i in final_prize:
            if i == '$':
                lista_precio2.append(final_prize)
            else:
                ''







lista_precio2= cleaning_list(lista_precio2, '\n')
lista_nombres2= cleaning_list(lista_nombres2, '\n')


for i in (lista_nombres2):
    if i == '':
        lista_nombres2.remove(i)


for i in range(51):
    precio= lista_precio2[i]
    nombre= lista_nombres2[i]
    dict_vit['categoria']= ('vitaminas')
    dict_vit['producto']= coding.onEncrypt(nombre)
    dict_vit['precio']= precio

    database.child('Farma Listo').push(dict_vit)


#Termina la parte de vitaminas y empieza la parte de salud sexual

url= "https://www.farmalisto.com.mx/2190-salud-sexual"

response= requests.get(url)

soup= BeautifulSoup(response.text, 'html.parser')

sexual= soup.find(id= "js-product-list").find_all('article')

dict_ss= {}

lista_nombres3= []

lista_precio3= []


for i,c in enumerate(sexual):

    h2s= c.find_all('h2')

    for j, k in enumerate(h2s):
        final_name= k.getText().rstrip("\n").replace(',','').replace('+','')

        lista_nombres3.append(final_name)


for i, a in enumerate(sexual):
    spans= a.find_all('span')

    for j, b in enumerate(spans):
        final_prize= b.getText().rstrip("\n").replace(',','').replace('+','')
        for i in final_prize:
            if i == '$':
                lista_precio3.append(final_prize)
            else:
                ''







lista_precio3= cleaning_list(lista_precio3, '\n')
lista_nombres3= cleaning_list(lista_nombres3, '\n')


for i in (lista_nombres3):
    if i == '':
        lista_nombres2.remove(i)


for i in range(51):
    precio= lista_precio3[i]
    nombre= lista_nombres3[i]
    dict_ss['categoria']= ('salud sexual')
    dict_ss['producto']= coding.onEncrypt(nombre)
    dict_ss['precio']= precio

    database.child('Farma Listo').push(dict_ss)


#Termina la parte de salud sexual y empieza higiene y belleza

url= "https://www.farmalisto.com.mx/2110-higiene-y-belleza"

response= requests.get(url)

soup= BeautifulSoup(response.text, 'html.parser')

hyb= soup.find(id= "js-product-list").find_all('article')

dict_hyb= {}

lista_nombres4= []

lista_precio4= []


for i,c in enumerate(hyb):

    h2s= c.find_all('h2')

    for j, k in enumerate(h2s):
        final_name= k.getText().rstrip("\n").replace(',','').replace('+','')

        lista_nombres4.append(final_name)


for i, a in enumerate(hyb):
    spans= a.find_all('span')

    for j, b in enumerate(spans):
        final_prize= b.getText().rstrip("\n").replace(',','').replace('+','')
        for i in final_prize:
            if i == '$':
                lista_precio4.append(final_prize)
            else:
                ''







lista_precio4= cleaning_list(lista_precio4, '\n')
lista_nombres4= cleaning_list(lista_nombres4, '\n')


for i in (lista_nombres4):
    if i == '':
        lista_nombres4.remove(i)


for i in range(51):
    precio= lista_precio4[i]
    nombre= lista_nombres4[i]
    dict_hyb['categoria']= ('higiene y belleza')
    dict_hyb['producto']= coding.onEncrypt(nombre)
    dict_hyb['precio']= precio

    database.child('Farma Listo').push(dict_hyb)



# Termina la parte de higiene y belleza y empieza la parte final de bebés

url= "https://www.farmalisto.com.mx/1915-bebes"

response= requests.get(url)

soup= BeautifulSoup(response.text, 'html.parser')

bb= soup.find(id= "js-product-list").find_all('article')

dict_bb= {}

lista_nombres5= []

lista_precio5= []


for i,c in enumerate(bb):

    h2s= c.find_all('h2')

    for j, k in enumerate(h2s):
        final_name= k.getText().rstrip("\n").replace(',','').replace('+','')

        lista_nombres5.append(final_name)


for i, a in enumerate(bb):
    spans= a.find_all('span')

    for j, b in enumerate(spans):
        final_prize= b.getText().rstrip("\n").replace(',','').replace('+','')
        for i in final_prize:
            if i == '$':
                lista_precio5.append(final_prize)
            else:
                ''







lista_precio5= cleaning_list(lista_precio5, '\n')
lista_nombres5= cleaning_list(lista_nombres5, '\n')


for i in (lista_nombres5):
    if i == '':
        lista_nombres5.remove(i)


for i in range(51):
    precio= lista_precio5[i]
    nombre= lista_nombres5[i]
    dict_bb['categoria']= ('bebes')
    dict_bb['producto']= coding.onEncrypt(nombre)
    dict_bb['precio']= precio

    database.child('Farma Listo').push(dict_bb)
