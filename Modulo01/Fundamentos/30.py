'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''
n = int(input('Número inteiro: '))
if n % 2 != 0:
    print(f'O número {n} é IMPAR.')
else:
    print(f'O número {n} é PAR')
