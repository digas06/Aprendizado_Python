'''Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.'''
from math import trunc

num = float(input('Digite um número fracionário: '))
print(f'Porção inteira: {trunc(num)}')
print(f'Porção interia: {num // 1:.0f}')
