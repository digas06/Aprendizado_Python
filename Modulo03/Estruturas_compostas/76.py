'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
 na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''
lista = ('Lápis', 1.50, 'Caneta', 2.00, 'Caderno', 20.00,
         'Mochila', 50.00, 'Estojo', 8.00, 'Borracha', 1.00)
print(
    f'\033[1m{"-=-"*17}\n\033[0m{"Listagem de preços":^40}\n\033[1m{"-=-"*17}\033[0m')
for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<40}', end='')
    elif c % 2 != 0:
        print(f'R${lista[c]:>7.2f}')

print(f'\033[1m{"-=-"*17}\033[0m')
