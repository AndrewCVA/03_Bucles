'''
Escriba un programa para hacer un patrón como una pirámide con números aumentados en 1
   1
  2 3
 4 5 6
7 8 9 10
'''

#Entrada

altura = 4
n = 0

#Proceso/Salida

for i in range(1, altura +1):
    for j in range(altura - i):
        print(" ", end="")
    for j in range(1, i+1):
        n = n+1
        print(f"{n} ", end="")
    print()