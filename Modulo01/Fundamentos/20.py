'''O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''
from random import shuffle
a1 = 'Ester'
a2 = 'Diego'
a3 = 'Karine'
a4 = 'Carla'
lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'A ordem será: {lista}')
