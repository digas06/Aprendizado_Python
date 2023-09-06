''' Crie um programa que leia o nome e o preço de vários produtos.
 O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''
somador = contador = barato_nome = barato_valor = cont = 0
while True:
    nome = input('Nome do produto: ')
    preço = float(input('Valor: '))
    somador += preço
    if preço > 1000:
        contador += 1
    escolha = input('Deseja continuar? [S/N]: ')
    print("-=-"*20)
    cont += 1
    if cont == 1 or preço < barato_valor:
        barato_valor = preço
        barato_nome = nome
    if escolha[0] in 'Nn':
        break
    elif escolha[0] not in 'SsNn':
        print('Programa encerrado. Resposta inválida')
        break
print(f'Gasto total: R${somador:.2f}')
print(f'Custaram mais que R$1000,00: {contador}')
print(f'Nome do mais barato: {(barato_nome).title()} Valor: R${barato_valor:.2f}')
