'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
 mostre uma mensagem dizendo que ele foi multado.
 A multa vai custar R$7,00 por cada Km acima do limite.'''
 # Ler a velocidade do carro:
velocidade = int(input('velocidade atual do carro: '))
 # determinar se ultrapassou 80km/h:
if velocidade > 80:
    # Se sim, mmostrar uma mensagem dizendo que foi multado:
    print('Multado! Você excedeu o limite de 80km/h.')
    # Mostrar o valor da multa:
    multa = (velocidade - 80) * 7
    print(f'Deverá pagar uma multa de R${multa:.2f}')
# Mostrar mensagem "Tenha um bom dia, dirija com segurança!"
print("Tenha um bom dia, dirija com segurança!")
