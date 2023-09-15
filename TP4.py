#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 18:44:48 2023

@author: martinahackbartt
"""

### STRINGS

cadena= '-1294'
cadena.isalpha()
cadena.isalnum()

cadena1= 'hola'
cadena2='hoLaAa'
cadena1.upper()
cadena2.lower()
cadena1.capitalize()
cadena2.title()

##EJEMPLO1
#OPCION 1
palabras= 'Automovil Club Argentino'
listadepalabras= palabras.split()
sigla= ''
for palabrita in listadepalabras:
    sigla+= palabrita[0]
    sigla.upper()

#OPCION 2
sigla= ''.join([p[0] for p in palabras.split()]).upper()

##EJEMPLO2
cadena1.rjust(10) #agrega espacios a la izq para llegar a 10 caracteres
cadena.ljust(10)

cadena2.rstrip('a') #elimina las ultimas a minúsculas si las hay
cadena2.lstrip('h') #elimino la primer o primeras h al inicio (izq)
'[1,2,3,4]'.strip('[]')

texto= 'Hola Mundo, Python! buen dia'

var1= texto.find('Python') #devuelve la posición o -1 si no la encuentra (viendo de izq a der)
var2= texto.rfind('o') #devuelve la posición viendo de der a izq (la primera q encuentra)
palabras.center(40) #centra el texto en una cantidad de caracteres

dia= 16
mes= 'Enero'
cad= f'Sucedio el {dia} de {mes}'
cad2= f'{dia:05}' #agrego 0s para que el numero tenga 05 cantidad de digitos

pi= 3.1416
cad3= f'{pi:.2f}'

### Ejercicio 3
# Funcion a la que le doy una clave maestra y genera 2 claves, una con los nros impares y otra con los pares
def claveMaestra(clave):
    clave1= ''
    clave1+= ''.join([clave[i] for i in range(len(clave)) if i % 2 == 0])
    clave2= ''
    clave2+= ''.join([clave[i] for i in range(len(clave)) if i % 2 != 0])
    return clave1, clave2

maestra= '29482848290489'
buscoClaves= claveMaestra(maestra)
print(buscoClaves)

### Ejercicio 4
# Convertir un numero a número romano
def numeroRomano(cad):
    if len(cad)==4:
        miles= 'M'*int(cad[0])
        cientos= 'C'*int(cad[1])
        decenas= 'X'*int(cad[2])
        unidades= 'I'*int(cad[3])
        numero= ''.join([miles,cientos,decenas,unidades])
    elif len(cad)==3:
        cientos= 'C'*int(cad[0])
        decenas= 'X'*int(cad[1])
        unidades= 'I'*int(cad[2])
        numero= ''.join([cientos,decenas,unidades])
    elif len(cad)==2:
        decenas= 'X'*int(cad[0])
        unidades= 'I'*int(cad[1])
        numero= ''.join([decenas,unidades])
    else:
        unidades='I'*int(cad[0])
        numero= ''.join([unidades])
    return numero

numero= '2320'
romanos= numeroRomano(numero)
print(romanos)

### Ejercicio 8
# Función que reciba cadena de caracteres con varias palabras y devuelva las palabras ordenadas en orden alfabetico

def ordenAlfabetico(cad):
    listaPalabras=cad.split()
    ordenada= sorted(listaPalabras)
    ordenada= ' '.join(ordenada)
    return ordenada

ejemplo= ordenAlfabetico('Pablito clavó un clavito')
print(ejemplo)
    
