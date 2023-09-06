'''Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120'''
n = int(input('Número: '))
contador = n
fatorial = 1
print(f'{n}! = ', end='')
while contador > 1:
    print(f'{contador}', end=' X ')
    fatorial *= contador
    contador -= 1
print(f'1 = {fatorial}')
