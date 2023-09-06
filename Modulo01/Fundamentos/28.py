''' Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-'*20)
print('''Vou escolher um número de 0 a 5. Tente adivinha-lo:''')
print('-=-'*20, "\n...")
sleep(3)
jogador = int(input('Sua tentativa: '))
if jogador == computador:
    print('Parabéns, você acertou!')
elif jogador > 5 or jogador < 0:
    print('Resposta inválida!')
else:
    print('Você errou.')
