'''Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''

valor = float(input('Valor do produto: '))
print(f'R${valor:.2f} - 5% = R${valor - (valor*5/100):.2f}')
