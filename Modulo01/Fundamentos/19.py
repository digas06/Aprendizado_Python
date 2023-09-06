'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
 lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''
import random
a1 = 'Carla'
a2 = 'Karine'
a3 = 'Ester'
a4 = 'Diego'
lista = [a1, a2, a3, a4]
print(f'Aluno escolhido: {random.choice(lista)}')
