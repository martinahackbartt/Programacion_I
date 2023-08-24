#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 11:50:24 2023

@author: martinahackbartt
"""

##Ejercicio 1
#La función recibe de input 3 números enteros positivos
# Devuelve un número entero positivo que corresponde al mayor de los 3 números del input
# Si no hay mayor estricto, devuelve -1
# Proceso: evalúo entre x,y quien es el mayor, y luego lo comparo con z. 
def mayor_de_los_tres(x,y,z):
    mayor_relativo= -1
    if x>y:
        mayor_relativo=x
        if z>mayor_relativo:
            mayor_relativo= z
    elif y>x:
        mayor_relativo=y
        if z>mayor_relativo:
            mayor_relativo= z
    return mayor_relativo
    
prueba= mayor_de_los_tres(2,2,2)   
if prueba==-1:
     print('No hay número mayor estricto')
else:
    print('El número mayor es:', prueba)


##Ejercicio 2
#La función recibe de input 3 números enteros correspondientes a dia, mes y año.
# Devuelve True (1) si se corresponde a una fecha correcta o False (0) si la fecha es inválida. 
#Tenemos en cuenta cualquier año, pasado o futuro del 1800 al 2100
def fechavalida(dia,mes,año):
    veredicto= 0
    #caso febrero, bisiesto y no bisiesto
    if mes==2 and dia==29:
        if año%4==0 and año%100!=0 and año in range(1800,2101):
            veredicto+=1
    elif mes==2 and dia in range(1,29) and año in range(1800,2101):
        veredicto+=1
    #caso meses con 31 dias
    elif mes in [1,3,5,7,9,11]:
        if dia in range(1,32) and año in range(1800,2101):
            veredicto+=1
    #caso meses con 30 dias
    elif mes in [4,6,8,10,12]:
        if dia in range(1,31)and año in range(1800,2101):
            veredicto+=1
    else:
        veredicto+=0
    return veredicto
    
ver = fechavalida(1,15,2022)
if ver==1:
    print("Esta fecha es válida!")
else:
    print("Fecha Inválida")

## Ejercicio 3
#Datos entrada: número entero positivo que representa a la cantidad de viajes realizados por mes
#Datos salida: número real positivo que representa el total gastado en viajes
#Proceso: se evalua la cantidad de viajes, y a partir de eso se calcula la tarifa aplicada y se multiplica por la cantidad de viajes realizados. 
#Atención: se asume que a partir de una cantidad de viajes TODOS los boletos tienen el descuento que se menciona

def total_gastado(viajes):
    tarifa_maxima=100
    if viajes<21:
        return viajes*tarifa_maxima
    elif 21<viajes<31:
        return viajes*(tarifa_maxima*0.80)
    elif 31<viajes<41:
        return viajes*(tarifa_maxima*0.70)
    else:
        return viajes*(tarifa_maxima*0.60)

gastos= total_gastado(30)
print('Los gastos totales fueron de:', gastos)

## Ejercicio 4
#Datos entrada: 2 números enteros (1 es el total de la compra y 2 es el dinero recibido)
#Datos salida: una lista cuyos valores corresponden a cada billete que se debe entregar y el total de cambio
#Proceso: decidir cuanto dinero debe otorgarse al cliente y luego elegir la cantidad de billetes
#de cada notación que van a entregarse, minimizando la cantidad de billetes
def cambio(totalcompra,dinerorecibido):
    lista_cambio= []
    vuelto_restante= dinerorecibido-totalcompra
    #caso en el cual el dinero no es suficiente
    if dinerorecibido<totalcompra:
        return -1
    while vuelto_restante>=500:
        lista_cambio.append(500)
        vuelto_restante-=500
    while vuelto_restante>=100:
        lista_cambio.append(100)
        vuelto_restante-=100
    while vuelto_restante>=50:
        lista_cambio.append(50)
        vuelto_restante-=50
    while vuelto_restante>=20:
        lista_cambio.append(20)
        vuelto_restante-=20
    while vuelto_restante>=10:
        lista_cambio.append(10)
        vuelto_restante-=10
    while vuelto_restante>=5:
        lista_cambio.append(5)
        vuelto_restante-=5
    while vuelto_restante>=1:
        lista_cambio.append(1)
        vuelto_restante-=1
    return lista_cambio
    
cambio= cambio(800,2101)    
if cambio==-1:
    print('El dinero recibido no es suficiente!')
else:
    print('Se le debe dar al cliente un total de', sum(cambio),'.', 'Los billetes a otorgar son:',cambio)

## Ejercicio 5
# Datos entrada: número natural que describe la cantidad de filas
# Datos salida: string de asteriscos con tantas filas como dice la entrada
# Proceso: generar una linea de x asteriscos por cada fila que se pide segun input. 
#Para el caso 1 siempre son 10 asteriscos y para el 2do,la cantidad de asteriscos crece de 2 en 2

#1ra función
def asteriscos_1(filas):
    if filas <= 0:
        return "Número de filas debe ser mayor que 0"
    resultado = ""
    for i in range(filas):
        resultado += "*" * 10 + "\n"  # Genera una fila de 10 asteriscos y agrega un salto de línea
    return resultado

patron_1= asteriscos_1(5)
print(patron_1)

#2da función
def asteriscos_2(filas):
    if filas <= 0:
        return "Número de filas debe ser mayor que 0"
    resultado = ""
    for i in range(filas+1):
        resultado += "*" * (i*2) + "\n"  # Genera una fila de 10 asteriscos y agrega un salto de línea
    return resultado

patron_2= asteriscos_2(5)
print(patron_2)

## Ejercicio 6
# Datos de entrada: 2 numeros enteros positivos
# Datos de salida: 1 número entero positivo
# Proceso: convierto a los 2 numeros enteros en strings para sumarlos y que queden seguidos los números. Luego vuelvo a convertir a int
def concat(nro1,nro2):
    resultado= str(nro1)
    resultado += str(nro2)
    resultado= int(resultado)
    return resultado

conc= concat(1234,567)
print(conc)

## Ejercicio 7
#asumimos 28 días para febrero, no tenemos en cuenta años bisiestos.
def diasiguiente(dia,mes,año):
    while fechavalida(dia, mes, año)==1: #verifiquemos que la fecha sea valida!, si es invalida func devuelve None
        nuevodia= dia
        nuevomes= mes
        nuevoaño= año
        if mes==2:
            if dia<28:
                nuevodia=dia+1
            elif dia==28:
                nuevodia=1
                nuevomes= mes+1
        #caso diciembre
        elif mes==12:
            if dia<30:
                nuevodia=dia+1
            elif dia==30:
                nuevodia=1
                nuevomes=1
                nuevoaño=año+1
        #caso meses con 31 dias
        elif mes in [1,3,5,7,9,11]:
            if dia<31:
                nuevodia=dia+1
            elif dia==31:
                nuevodia=1
                nuevomes=mes+1
        #caso meses con 30 dias
        elif mes in [4,6,8,10]:
            if dia<30:
                nuevodia=dia+1
            elif dia==30:
                nuevodia=1
                nuevomes=mes+1
        return nuevodia, nuevomes, nuevoaño

masuno= diasiguiente(30,12,2023)
print(masuno)   
         
# Sumar N días a una fecha
n= 10
dia,mes,año= 30,12,2002
for i in range(0,n):
    dia,mes,año= diasiguiente(dia,mes,año)
mas_n= dia,mes,año
print(mas_n)
        
#Calcular dias existentes entre una fecha y otra
fecha1=30,12,2002
fecha2=30,12,2003
#primero vamos a ver qué fecha es anterior
if fecha1[2]<fecha2[2]:
    fecha_anterior= fecha1
    fecha_posterior= fecha2
elif fecha1[2]>fecha2[2]:
    fecha_anterior= fecha2
    fecha_posterior= fecha1
else:
    if fecha1[1]<fecha2[1]:
        fecha_anterior= fecha1
        fecha_posterior= fecha2
    elif fecha1[1]>fecha2[1]:
        fecha_anterior= fecha2
        fecha_posterior= fecha1
    else:
        if fecha1[0]<fecha2[0]:
            fecha_anterior= fecha1
            fecha_posterior= fecha2
        elif fecha1[0]>fecha2[0]:
            fecha_anterior= fecha2
            fecha_posterior= fecha1

i = 0
while fecha_anterior != fecha_posterior:
    fecha_anterior = diasiguiente(fecha_anterior[0], fecha_anterior[1], fecha_anterior[2])
    i += 1
print("Número de días entre las fechas=", i)
        
## Problema 8
def diadelasemana(dia,mes,año):
    if mes<3:
        mes= mes+10
        año= año-1
    else:
        mes= mes-2
    siglo= año//100
    año2= año % 100
    diasem= (((26*mes-2)//10)+dia+año2+(año2//4)+(siglo//4)-(2*siglo))%7
    if diasem<0:
        diasem= diasem+7
    return diasem

dia,mes,año= 1,8,2023

calendario= [[[],[],[],[],[],[],[]],
             [[],[],[],[],[],[],[]],
             [[],[],[],[],[],[],[]],
             [[],[],[],[],[],[],[]],
             [[],[],[],[],[],[],[]]]

for i in range(1,8-diadelasemana(dia, mes, año)):
    calendario[0][diadelasemana(dia,mes,año)].append(i)
    dia=dia+1

    
for m in range(1,5):
    for f in range(0,7):
        i+=1
        calendario[m][f].append(i)

print('')
print("  Do   Lu   Ma   Mi   Ju   Vi   Sa")
print("-" * 35)  # Ajustar el número de guiones según la alineación
for semana in calendario:
    for dia in semana:
        # Si la celda contiene una lista y la lista no está vacía, imprime el primer elemento.
        valor = dia[0] if isinstance(dia, list) and dia else ' '
        print(f"{valor:>3}", end="  ")
    print()  # Cambiar a la siguiente línea después de que toda la semana haya sido impresa
