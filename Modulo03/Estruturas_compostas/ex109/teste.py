'''Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no 
desafio 108.'''
import moeda  


numero = float(input('Número: '))

print(f'R$ {moeda.moeda(numero)} + 10% = {moeda.aumentar(numero, 10, True)}')

print(f'R$ {moeda.moeda(numero)} - 10% = {moeda.diminuir(numero, 10, True)}')

print(f'R$ {moeda.moeda(numero)} X 2 = {moeda.dobro(numero,True)}')

print(f'R$ {moeda.moeda(numero)} / 2 = {moeda.metade(numero,True)}')
