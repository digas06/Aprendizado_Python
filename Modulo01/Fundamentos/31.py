'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, 
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''
d = float(input('Distância da viagem em km: '))
if d <= 200:
    valor = d * 0.50
if d > 200:
    valor = d * 0.45
print(f'Distância {d}km\nValor a ser pago: R${valor:.2f}')
