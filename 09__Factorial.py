'''
Escriba un programa para calcular el factorial de un número dado.
'''

#Entrada

factor = 1
cont = 1
n = int(input("Ingrese un numero entero: "))

#Proceso/Salida

while cont <= n:
    factor = factor * cont
    print(factor)
    cont = cont + 1
print(f"El factorial de {n} es = {factor}")