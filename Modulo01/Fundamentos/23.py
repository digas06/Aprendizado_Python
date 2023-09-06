'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.'''
# Ler um número de até 4 digitos:
n = int(input('Digite um número inteiro de 0 a 9999: '))
# Separar cada um dos dígitos:
unidade = n // 1 % 10
dezena = n // 10 % 10
centena = n // 100 % 10
milhar = n // 1000 % 10
# Mostrar na tela:
print(f'Milhar: {milhar}\nCentena: {centena}\nDezena: {dezena}\nUnidade: {unidade}')
