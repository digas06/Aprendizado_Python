'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de 
cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''
lista = []
dic = {}
contador_mulheres = 0
while True:
    dic['Nome'] = input('Nome: ').strip().title()
    dic['Sexo'] = input('Sexo [F/M]: ').strip().upper()
    while dic['Sexo'][0] not in 'FM':
        dic['Sexo'] = input(
            'Opção inválida. Digite o sexo novamente [F/M]: ').strip().upper()
    if dic['Sexo'] == 'F':
        contador_mulheres += 1
    dic['Idade'] = int(input('Idade: '))
    lista.append(dic.copy())
    escolha = input('Quer continuar? [S/N]: ').lower().strip()
    while escolha[0] not in 'sn':
        escolha = input(
            'Opção inválida. Deseja continuar? [S/N]: ').lower().strip()
    print('-'*25)
    if escolha in 'n':
        break
print(f'Número de cadastros: {len(lista)}')
soma = 0
for c in lista:
    soma += c['Idade']
print(f'Média de idades: {soma/len(lista):.0f}')
if contador_mulheres > 0:
    print(f'Mulheres cadastradas: ', end='')
    for s in lista:
        if s['Sexo'] == 'F':
            print(f'{s["Nome"]}', end=', ', sep='')
print(f'\n{"-"*30}')
print('\nPessoas acima da média: ')
for p in lista:
    if p['Idade'] > soma / len(lista):
        print(f'Nome: {p["Nome"]} ==> {p["Idade"]} Sexo: {p["Sexo"]}')
print('-='*20)
 
