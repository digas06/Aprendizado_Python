'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
escolha = 0
while escolha != 5:
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    escolha = int(input('Sua escolha: '))
    if escolha == 1:
        print(f'{v1} + {v2} = {v1+v2}')
    if escolha == 2:
        print(f'{v1} X {v2} = {v1*v2}')
    if escolha == 3:
        if v1 > v2:
            print(f'Maior: {v1}')
        else:
            print(f'Maior: {v2}')
    if escolha == 4:
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
print('Fim do programa!')