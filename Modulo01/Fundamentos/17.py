''' Faça um programa que leia o comprimento do cateto 
oposto e do cateto adjacente de um triângulo retângulo.
 Calcule e mostre o comprimento da hipotenusa.'''
import math
# Ler o comprimento do cateto oposto:
c1 = float(input('Cateto oposto: '))
# Ler o comprimento doc ateto adjacente:
c2 = float(input('Cateto adjacente: '))
# Mostrar o comprimento da hipotenusa:
hipo = ((c1**2) + (c2**2))**(1/2)
print(f'{hipo}')
print(math.hypot(c1, c2))
