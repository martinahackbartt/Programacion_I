#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 19:06:43 2023

@author: martinahackbartt
"""

## Ejercicio 1
#a
import numpy as np
def cargarnumeros(n):
    lista=[]
    for i in range(0,n):
        numero=np.random.randint(1000,10000)
        lista.append(numero)
    return lista

lista_a= cargarnumeros(10)
print(lista_a)

#b
def sumlista(lista):
    return sum(lista) #esto es legal? jajaja

suma= sumlista(lista_a)
print(suma)

#c
def eliminar(lista, x):
    while x in lista:
        if x in lista:
            lista.remove(x)
    return lista
lista_prueba= [9873, 6363, 6814, 6363, 5598, 6180, 9940, 9209, 8002, 2984, 9826]
lista_c= eliminar(lista_prueba,6363)
print(lista_c)

#d 
def escapicua(lista):
    capicua= 0
    i=0
    j=-1
    for _ in range(round(len(lista)/2)):
        if lista[i]==lista[j]:
            capicua=1
            i+=1
            j+=-1
        else:
            capicua=0
    return capicua

print('')
capicua=escapicua([50,17,91,17,50])        
if capicua==0:
    print('La lista no es capicúa!')
else:
    print('La lista es capicúa!')
    
## Ejercicio 2
#a
def cincuenta_aleatorios():
    lista=[]
    for i in range(50):
        numero=np.random.randint(1,101) #pongo 101 para que incluya al 100
        lista.append(numero)
    return lista
    

#b
def repetidos(lista):
    repes= 0
    for i in range(len(lista)):
        valor= lista[i]
        if valor in lista[i+1:]: #chequeamos si el valor se repite desde esa posicion en adelante
            repes=1
        else:
            repes+=0
    return repes

#c
#esto sería el equivalente de lista.set()
def unicos(lista):
    unicos=[]
    for i in range(0,len(lista)):
        valor= lista[i]
        if valor not in unicos:
            unicos.append(valor)
    return unicos

print('')      
cincuenta= cincuenta_aleatorios()
print(cincuenta)
repetidos= repetidos(cincuenta)
unicos= unicos(cincuenta)
if repetidos==0:
    print('No hay repetidos!')
else:
    print('Hay repetidos, esta es la lista nueva:')
    print(unicos)

## Problema 3
def cuadrados(n):
    cuadraditos=[]
    for i in range(1,n+1):
        cuadraditos.append(i**2)
    return cuadraditos   

cuadrados= cuadrados(20)   
print('')
print('Lista de cuadrados') 
print(cuadrados)

## Problema 4
def eliminar_repes(lista1,lista2):
    for i in range(len(lista2)):
        valor= lista2[i]
        while valor in lista1:
            lista1.remove(valor)
    return lista1

sinrepes= eliminar_repes([1,2,3,4,5,6,7],[1,2,3])
print('')
print(sinrepes)

## Problema 5
def ordenada(lista):
    veredicto= 0
    for i in range(len(lista)-1):
        if lista[i] <= lista[i+1]:
            veredicto+=1
        else:
            veredicto+=0
    if veredicto==(len(lista)-1):
        veredicto=1
    else:
        veredicto=0
    return veredicto

print('')
lista_1 =[1, 2, 3, 4, 5]
prueba1=ordenada(lista_1)
if prueba1==0:
    print('La lista', lista_1, 'no está ordenada')
else:
    print('La lista', lista_1, 'está ordenada')
lista_2 =['b', 'a']
prueba2=ordenada(lista_2)
if prueba2==0:
    print('La lista', lista_2, 'no está ordenada')
else:
    print('La lista', lista_2, 'está ordenada')


## Problema 6
def normalizar(lista):
    sumatot= 0
    lista_new= []
    for i in lista:
        sumatot+= lista[i]
    for j in lista:
        lista_new.append(lista[j]/sumatot)
    return lista_new   
      
listita=[1,1,2]  
listanorm= normalizar(listita)
print('')
print('Lista original:',listita)
print('Lista normalizada:',listanorm)