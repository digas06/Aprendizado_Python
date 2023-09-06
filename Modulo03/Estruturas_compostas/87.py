''' Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''
matriz = [[], [], []]
soma_pares = soma_coluna = 0

for p in range(3):
    for i in range(3):
        n = int(input(f'Digite um valor para a posição [{p}, {i}]: '))
        matriz[p].append(n)
        if i == 2:
            soma_coluna += n
        if n % 2 == 0:
            soma_pares += n
for p in range(3):
    for i in range(3):
        print(f'[{matriz[p][i]:^5}]', end=' ')
    print()
print('-='*20)
print(f'Soma dos pares: {soma_pares}')
print(f'Soma da terceira coluna: {soma_coluna}')
print(f'Maior da 2ª coluna: {max(matriz[1])}')
