'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a 
quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
 sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

# Perguntar a quantidade de km rodados:
km = float(input('Km rodado: '))
vkm = km * 0.15
# Perguntar a quantidade de dias:
d = float(input('Dias que esteve alugad:'))
vd = d * 60
# Calcular o preço a pagar: 60 por dia e 0.15 por km
print(f'Valor por dia: R${vd:.2f}\nValor por km: R${vkm:.2f}\nTotal a pagar: R${vd + vkm:.2f}')
