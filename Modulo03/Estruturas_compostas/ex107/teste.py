'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() 
e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.'''
import moeda

numero = float(input('Número: '))

print(f'{numero} + 10% = {moeda.aumentar(numero, 10)}')

print(f'{numero} - 10% = {moeda.diminuir(numero, 10)}')

print(f'{numero} X 2 = {moeda.dobro(numero)}')

print(f'{numero} / 2 = {moeda.metade(numero)}')
