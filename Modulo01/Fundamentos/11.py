'''Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.'''

larg = float(input('Largura: '))
alt = float(input('Altura: '))

area = larg * alt

print(f'Área: {area}m²\nLatas de tinta: {area / 2:.1f}')
