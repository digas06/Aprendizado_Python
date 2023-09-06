''' Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. '''
lista = []
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Número para a posição {c}: ')))
    if c == 0:
        maior = lista[c]
        menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print('-=-'*20)
print(f'Maior número: {maior} \nPosição: ', end='')
for pos, c in enumerate(lista):
    if c == maior:
        print(f'{pos}...', end=' ')
print(f'\n{"-=-"*20}')
print(f'Menor número: {menor} \nPosição: ', end='')
for pos, c in enumerate(lista):
    if c == menor:
        print(f'{pos}...', end='')
