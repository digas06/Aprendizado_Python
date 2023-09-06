'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
 Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, 
 sabendo que o vencedor tirou o maior número no dado.'''
from random import randint
from time import sleep
from operator import itemgetter
dic = {}
print(f'Valores sorteados:\n{"-="*20}')
for c in range(1, 5):
    dic[f'Jogador {c}'] = randint(1, 6)
for chave, valor in dic.items():
    print(f'{chave} sorteou: {valor}')
    sleep(1)
print('-='*20)
print('\t==    Ranking     ==')
ranking = sorted(dic.items(), key = itemgetter(1), reverse=True)
for posição in range(4):
    print(f'{posição+1}º {ranking[posição][0]}: {ranking[posição][1]}.')
    sleep(1)
