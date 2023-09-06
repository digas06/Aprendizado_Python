# Crie um programa que leia o nome completo de uma pessoa e mostre:
nome = input('Nome completo: ').strip() 
# - O nome com todas as letras maiúsculas e minúsculas.
print(f'Letra maiúsculas: {nome.upper()}\nLetras minúsculas: {nome.lower()}')
# - Quantas letras ao todo (sem considerar espaços).
not_space = ''.join(nome.split(' '))
print(f'Quantidade de letras: {len(not_space)}')
# - Quantas letras tem o primeiro nome.
primerito_nome = nome.split()
print(f'O primeiro nome tem {len(primerito_nome[0])} letras')
