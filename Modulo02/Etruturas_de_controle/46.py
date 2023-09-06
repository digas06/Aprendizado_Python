'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, 
indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''
from time import sleep
contador = 10
for c in range(0, 11):
    print(contador)
    sleep(1)
    contador -= 1
print('Boooooom!')
