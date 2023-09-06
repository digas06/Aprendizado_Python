'''Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros.'''
valor = float(input('Valor da compra: '))
print('''    [ 1 ] À vista dinheiro/cheque: -10%
    [ 2 ] Á vista no cartão: -5%
    [ 3 ] Em até 2x no cartão: preço formal
    [ 4 ] 3x ou mais no cartão: +20%''')
forma =  int(input('Forma de pagamento: '))
if forma == 1:
    print(f'Total a ser pago: R${valor - (valor*10/100):.2f}')
elif forma == 2:
    print(f'Total a ser pago: R${valor - (valor*5/100):.2f}')
elif forma == 3 or forma == 4:
    parcela = int(input('Número de parcelas: '))
    if parcela <= 2:
        print(f'Total a ser pago: R${valor}')
    elif parcela > 2:
        print(f'Total a se pago: R${valor + (valor*20/100):.2f}')
        print(f'{parcela}X R${(valor + (valor*20/100))/parcela:.2f}')
else:
    print('Forma de pagamento inválida.')