'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.'''
nome = input('Nome completo: ').strip().lower()
print(f'Tem "Silva"? {"silva" in nome}')
