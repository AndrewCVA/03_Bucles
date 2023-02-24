'''
Escriba un programa para mostrar la tabla de multiplicar de un entero dado.
'''
#Entrada

x = 1

n = int(input("Ingrese un numero: "))

#Proceso/Salida

while x <= 10:
    print(f"{n} x {x} = {n*x}")
    x = x+1