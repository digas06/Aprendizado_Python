''' Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.'''

sa = float(input('Salário: R$'))
print(f'Antigo salário: R${sa:.2f}\nSalário com 15% de almento: R${sa + (sa*15/100):.2f}')
