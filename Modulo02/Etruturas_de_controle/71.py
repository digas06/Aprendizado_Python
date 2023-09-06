'''Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar 
quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
valor = int(input('Valor a sacar: '))

lista = [50, 20, 10, 1]
for c in lista:
    cinquenta = valor // c
    valor -= (cinquenta * c)

    vinte = valor // c
    valor -= (vinte * c)

    dez = valor // c
    valor -= (dez * c)

    um = valor // c
    valor -= (um * c)

    print(cinquenta)
    print(vinte)
    print(dez)
    print(um)
print(f'Notas de R$50: {cinquenta}')
print(f'Notas de R$20: {vinte}')
# print(f'Notas de R$10: {}')
# print(f'Notas de R$1: {}')
