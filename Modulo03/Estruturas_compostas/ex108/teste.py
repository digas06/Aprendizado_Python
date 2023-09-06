''' Adapte o código do desafio #107, criando uma função adicional chamada moeda() 
que consiga mostrar os números como um valor monetário formatado.'''
import moeda


numero = float(input('Número: '))

print(f'R$ {moeda.moeda(numero)} + 10% = {moeda.moeda(moeda.aumentar(numero, 10))}')

print(f'R$ {moeda.moeda(numero)} - 10% = {moeda.moeda(moeda.diminuir(numero, 10))}')

print(f'R$ {moeda.moeda(numero)} X 2 = {moeda.moeda(moeda.dobro(numero))}')

print(f'R$ {moeda.moeda(numero)} / 2 = {moeda.moeda(moeda.metade(numero))}')
