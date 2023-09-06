'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''
numero = int(input('Numero inteiro: '))
cont = 0
for c in range(1, numero+1):
    if numero % c == 0:
        cont += 1
        print(f'\033[31m', end=' ')
    else:
        print('\033[33m', end=' ')
    print(f'{c}', end=' ')
if cont > 2:
    print(f'\n\033[0mO número: {numero} não é primo.')
else:
    print(f'\nO número: {numero} é primo.')