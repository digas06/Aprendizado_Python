'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''
import datetime

ano = int(input('Digite um ano (coloque 0 para analizar o ano atual): '))

if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')
