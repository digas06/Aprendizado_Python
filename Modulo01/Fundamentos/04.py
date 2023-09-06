'''Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu 
tipo primitivo e todas as informações possíveis sobre ele.'''
item = input('Digite algo: ')

print(f'Tipo primitivo: {type(item)}')
print(f'É somente espaços? {item.isspace()}')
print(f'Está em maiúsculo? {item.isupper()}')
print(f'Está em minúsculo? {item.islower()}')
print(f'Começa com letra maiúscula? {item.istitle()}')
print(f'É um número? {item.isnumeric()}')
print(f'É alphanumérico? {item.isalnum()}')

