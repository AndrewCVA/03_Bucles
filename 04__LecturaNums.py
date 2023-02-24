'''
Escribe un programa para leer 10 números del teclado y encontrar su suma y promedio.
'''

#Entrada

i = 0
suma = 0

#Proceso

while i <= 10:
    num = int(input("Ingrese numero: "))
    suma = suma + num
    promedio = suma / 10
    i = i+1

#Salida

print(f"La suma de sus 10 numeros es {suma} y el promedio es {promedio} ")