'''
Escriba un programa para mostrar n términos de número natural y su suma (Fibonacci).
'''

#Entrada

n= int(input("ingrese numero de terminos para la sucesion: "))

a, b = 0, 1

#Proceso/Salida

for i in range(n):
    print(a, end=' ')
    a, b = b, a + b    