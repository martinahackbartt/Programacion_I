#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 19:30:26 2023

@author: martinahackbartt
"""

import random
## Ejercicio 3)
def matrizNxN(N): 
    matriz= [[0]* N for i in range(N)] #creamos la matriz usando replicacion y listas por comprension
    for i in range(N):
        for j in range(N):
            matriz[i][j]=random.randint(0, N**2)
    return matriz

#print(matrizNxN(3))
        
## Ejercicio 5)
def mostrar_butacas():
    butacas= [[0]* M for i in range(N)]
    return butacas

def reservar(matriz,butacaselect):
    fila,columna= butacaselect
    if matriz[fila][columna]==0:
        matriz[fila][columna]=1
        return True
    else:
        return False

#esta funcion llena n espacios al azar en una matriz
def cargar_sala(matriz,n):
    for k in range(n):
        filarandom=random.randint(0,(len(matriz))-1)
        columnarandom= random.randint(0,len(matriz[0])-1)
        matriz[filarandom][columnarandom]=1
    return matriz

def butacas_libres(matriz):
    contador= sum(fila.count(0) for fila in matriz)
    return contador
 
 
def butacas_contiguas(matriz):
    max_secuencia = 0
    coordenadas_max = (0, 0)
    for i,fila in enumerate(matriz):
        j = 0
        while j < len(fila) - 1:
            if fila[j] == 0 and fila[j + 1] == 0:
                coordenadas = (i, j)
                secuencia_actual = 0
                while j < len(fila) and fila[j] == 0: #sigo mientras no se haya cortado la seq de 0s
                    secuencia_actual += 1
                    j += 1
                if secuencia_actual > max_secuencia: #si alguna tiene la misma capacidad, se va a quedar con la primera q encontró
                    max_secuencia = secuencia_actual
                    coordenadas_max = coordenadas
            else:
                j += 1
    return max_secuencia, coordenadas_max if max_secuencia > 0 else None


N=5
M=7
butacas0= mostrar_butacas()
butacaselect= 3,2
reservar= reservar(butacas0,butacaselect)     
sala_cargada= cargar_sala(butacas0,5)
libres=butacas_libres(sala_cargada)
contiguas= butacas_contiguas(sala_cargada)
print('Hay', contiguas[0], 'butacas contiguas a partir de la fila',contiguas[1][0]+1,'asiento', contiguas[1][0]+1)
print(sala_cargada)