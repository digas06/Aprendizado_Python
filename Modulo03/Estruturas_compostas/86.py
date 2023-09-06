'''Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
 No final, mostre a matriz na tela, com a formatação correta.'''
matriz = [[], [], []]
for p in range(3):
    for i in range(3):
        matriz[p].append(int(input(f'Digite um número para [{p}, {i}]: ')))
print('-'*20)
for p in range(3):
    print()
    for i in range(3):
        print(f'[{matriz[p][i]}]', end=' ')
