'''
Escriba un programa para mostrar el patrón como triángulo con un asterisco. El patrón como:
*
**
***
****
*****
****
***
**
*
'''

#Entarada

ancho = int(input("Ancho del triangulo: "))

#Proceso/Salida

for i in range(1, ancho +1):
    for j in range(i):
        print("* ", end="")
    print()
    
for i in range(1, ancho):
    for j in range(ancho - i ):
        print("* ", end="")
    print()
    