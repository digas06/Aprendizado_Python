'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos 
jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista 
composta.'''
from random import randint
jogos = int(input('Número de jogos a ser gerados: '))
lista = []
lista_temp = []
cont = 0
print(f'{"-="*10:<} SORTEANDO {jogos} JOGOS  {"-="*10:>}')
for c in range(0, jogos):
    while True:
        numero = randint(1, 60)
        if numero not in lista_temp:
            lista_temp.append(numero)
            cont += 1
        if cont >= 6:
            break
    cont = 0
    lista_temp.sort()
    lista.append(lista_temp[:])
    lista_temp.clear()
    print(f'Lista {c+1}: {lista[c]}')
print(f'{"-="*10:<}  BOA SORTE! {"-="*10:>}')
