'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
 No final, mostre o conteúdo da estrutura na tela.'''
dic = {}

dic['nome'] = input('Nome do aluno: ')
dic['media'] = float(input('Média: '))

print('-='*20)

print(f'Nome: {dic["nome"]}\nMédia: {dic["media"]}')

if dic['media'] < 5:
    dic['Situação'] = 'Reprovado'

elif dic['media'] == 5:
    dic['Situação'] = 'Recuperação'

else:
    dic['Situação'] = 'Aprovado'
print(f'Situação: {dic["Situação"]}')
