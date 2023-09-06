'''Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
 respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''
lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Número: ')))
    escolha = input('Quer continuar? [S/N]: ').strip().lower()
    if escolha in 'n':
        break
print(f'Lista completa: {lista}')
for c in lista:
    if c % 2 == 0:
        pares.append(c)
print(f'Lista de pares: {pares}')
for c in lista:
    if c % 2 != 0:
        impares.append(c)
print(f'Lista dos ímpares: {impares}')
