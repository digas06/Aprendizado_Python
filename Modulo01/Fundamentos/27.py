'''Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.'''
nome = str(input('Nome completo: ')).lower().strip().split()
print(f'Primeiro nome: {nome[0].title()}\nÚltimo nome: {nome[-1].title()}')
