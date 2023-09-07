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

## puedo hacerlo sin hacer una funcion, directamente definiendo a la lista por comprensión
print('Lista de cuadrados 2') 
cuadrados2= [x**2 for x in range(6)]
print(cuadrados2)

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

## Problema 7
lista1= [8,3,1]
lista2= [5,9,7]

## Problema 8
lista8= [x for x in range(100,201)]
print(lista8)

## Problema 9
#A = int(input("Enter A: "))   
#B = int(input("Enter B: "))   

A=1
B=100

lista9 = [j for j in range(A, B) if j % 7 == 0 and j % 5 != 0]
print('')
print('Lista ejercicio 9')
print(lista9)

## Problema 10
lista_azar= [i for i in range(0,101)]
lista10= [i for i in lista_azar if i%2!=0]
print('')
print('Lista al azar:',lista_azar)
print('Lista de impares a partir de azar:',lista10)

## Problema 11

def validarAfiliado(nro_afiliado):
    return 1000 <= nro_afiliado <= 9999

def validarMotivo(motivo):
    return motivo in [0, 1]

def ingresoPacientes():
    pacientes_urgencias = []
    pacientes_turno = []

    nro_afiliado = int(input("Ingresá el nro de afiliado o -1 si querés salir: "))

    while nro_afiliado != -1:
        if validarAfiliado(nro_afiliado):
            motivo = int(input('Ingresá 0 si venís por una urgencia, 1 si tenés turno: '))

            if validarMotivo(motivo):
                if motivo == 0:
                    pacientes_urgencias.append(nro_afiliado)
                else:
                    pacientes_turno.append(nro_afiliado)
            else:
                print('El número ingresado no es correcto')
        else:
            print('El numero ingresado no es correcto!')

        nro_afiliado = int(input("Ingresá el nro de afiliado o -1 si querés salir: "))
                
    return pacientes_urgencias, pacientes_turno

def consultarAtenciones(pacientes_urgencias, pacientes_turno):
    while True:
        nro_afiliado = int(input("Ingresá el nro de afiliado o -1 para salir: "))
        if nro_afiliado == -1:
            break #ya se que no es buena practica pero justo para esto es muy oportuno jajaja
        urgencias = pacientes_urgencias.count(nro_afiliado)
        turnos = pacientes_turno.count(nro_afiliado)
        print(f"El paciente {nro_afiliado} se atendió {urgencias} veces por urgencias y {turnos} veces con turno.")

def main(): #MI FUNCION PRINCIPAL QUE EJECUTA EL RESTO. MUCHOS PRINT, I KNOW
    urgencias, turnos = ingresoPacientes()
    print('########### SISTEMA DE INGRESO DE PACIENTES ############')
    print("############# ESPACIO DEL ADMINISTRADOR ##############")
    print("\nPacientes de Urgencias:")
    for paciente in urgencias:
        print(paciente)
    print("\nPacientes con Turno:")
    for paciente in turnos:
        print(paciente)
    print("\nConsulta de atenciones por número de afiliado:")
    consultarAtenciones(urgencias, turnos)

