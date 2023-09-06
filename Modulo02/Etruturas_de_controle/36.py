'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''
valor = float(input('Valor da casa: '))
salario = float(input('Salário do cliente: '))
tempo = float(input('Em quantos anos pretende pagar: '))
prestacao = valor / (tempo*12)
if prestacao > (salario*(30/100)):
    print(f'\033[31mEMPRESTIMO NEGADO!\nO salário de R${salario:.2f} é muito baixo.\033[0m')
else:
    print(f'\033[32mEMPRÉSTIMO APROVADO!\nPrestação: {tempo*12:.0f} X R${prestacao:.2f}\033[0m')