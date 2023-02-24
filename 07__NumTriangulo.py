'''
Escriba un programa para mostrar el patrón como un triángulo rectángulo con un número
El patrón como:
1
12
123
1234
12345
'''

#Entrada

ancho = 5

#Proceso Salida

for i in range(1, ancho +1):
    for j in range(1, i+1):
        print(f"{j}", end="")
    print()