#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 21:01:21 2023

@author: martinahackbartt
"""

### Ejercicio 1
import random

def juegoCartas(jug):
    if 2<jug<7:
        manos= [[0] for n in range(jug)]
        numeros= [1,2,3,4,5,6,7,10,11,12]
        palos= ['espada','oro','copa','basto']
        cartasPasadas= []
        for i in range(jug):
            cartasJug= []
            while len(cartasJug)<3:
                num= random.choice(numeros)
                palo= random.choice(palos)
                carta= num,palo
                if carta not in cartasPasadas:
                    cartasJug.append(carta)
                cartasPasadas.append(carta)
            manos[i]= cartasJug
    else:
        manos= 0
    return manos


def main():
    jug= int(input('Ingrese el numero de jugadores (2 a 6 posibles):'))
    mano= juegoCartas(jug)
    if mano==0:
        print('El número de jugadores ingresado es incorrecto. Recuerde que solo pueden jugar de 2 a 6 jugadores')
    i=1
    for jugador in mano:
        print(f'Cartas del jugador {i}',jugador)
        i= i+1
#main()
    
### Ejercicio 2
def impresiones(hojas, copias):
    paginas= [i for i in range(1,hojas+1)]
    #Intercaladas
    Inter= paginas*copias
    #Sin intercalar
    NoInter= sorted(Inter.copy())
    return Inter, NoInter

def main():
    hojas= int(input('Ingrese la cantidad de páginas de su trabajo:'))
    copias= int(input('Ingrese el número de copias deseadas:'))
    imp= impresiones(hojas,copias)
    print('Páginas intercaladas',imp[0])
    print('Páginas No intercaladas',imp[1])            
    
main()