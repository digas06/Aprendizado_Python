''' Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno 
retangular (largura e comprimento) e mostre a área do terreno.'''

def area(lar, comp):
    print(f'Área de um terreno {lar}m x {comp}m = {lar*comp:.2f}m²')


def titulo(msg):
    print(f'{"-="*20}\n{msg}\n{"-="*20}')


titulo('Controle de terrenos')
lar = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
area(lar, comp)
