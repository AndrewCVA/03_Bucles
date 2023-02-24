"""
Escriba un programa para mostrar un patrón como Z con asteriscos

*******
     *
    *
   *
  *
 *
*******

"""

#Entrada

print ("* * * * * * *")
list_a = [" ", " ", " ", " ", " ", "*" ]
n_lim1 = 5
n_lim2 = 4

#Proceso

for x in range (6):
    print(*list_a)
    list_a[n_lim1] = " "
    n_lim1 = n_lim1 - 1
    list_a[n_lim2] = "*"
    n_lim2 = n_lim2 - 1

#Salida

print ("* * * * * * *")
