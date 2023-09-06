'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
 fim e passo. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''


def contador(a, b, c):
    lista = []
    if c == 0:
        c = 1
    elif c < 0:
        c = abs(c)
    if a > b:
        for v in range(b, a+1):
            lista.append(v)
        lista.sort(reverse=True)
    else:
        for valor in range(a, b+1):
            lista.append(valor)
    print(f'Contagem de {a} até {b}, de {c} em {c}:')
    for v in lista[0::c]:
        print(f'{v}', end=' ')
    print(f'FIM !\n{"-="*20}')


contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de brincar com a ordem: ')

contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
