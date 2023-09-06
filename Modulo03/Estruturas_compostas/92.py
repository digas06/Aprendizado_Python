''' Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
 em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
import datetime

dic = {
    'Nome': input('Nome: ').title().strip(),
    'Idade': int(input('Ano de nascimento: ')),
    'Carteira': int(input('Carteira de trabalho (0 não tem): '))   
}

dic['Idade'] = (datetime.date.today().year) - dic['Idade']

if dic['Carteira'] > 0:
    dic['Ano de contratação'] = int(input('Ano da contratação: '))
    dic['Salário'] = int(input('Salário: R$ '))
    dic['Aposentadoria'] = dic['Idade'] + (dic['Ano de contratação'] + 35) - (datetime.date.today().year)
print('-='*25)

for chave, valor in dic.items():
    print(f'{chave}: {valor}')
