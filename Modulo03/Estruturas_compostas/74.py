'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
 Depois disso, mostre a listagem de números gerados e também indique o menor e o 
 maior valor que estão na tupla.'''
from random import randint as rd
numeros = (rd(1, 10), rd(1, 10), rd(1, 10), rd(1, 10), rd(1, 10))
print('Lista de números:', end=' ')
for c in numeros:
    print(f'{c}', end=' ')
print(f'\nMaior: {max(numeros)}')
print(f'Menor: {min(numeros)}')
