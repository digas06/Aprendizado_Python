galera = []
pessoa = []
p = maiorp = menorp = 0
while True:
    pessoa.append(input('Nome: ').strip())
    pessoa.append(float(input('Peso: (Kg) ')))
    galera.append(pessoa[:])
    print(f'{pessoa[0]} cadastrado(a) com sucesso.')
    del pessoa[:]
    escolha = input('Quer continuar? [S/N]: ').lower().strip()
    if p == 0:
        maiorp = galera[p][1]
        nome = galera[p][0]
        menorp = galera[p][1]
        nomep = galera[p][0] 
    else:
        if galera[p][1] > maiorp:
            maiorp = galera[p][1]
            nome = galera[p][0]
        if galera[p][1] < menorp:
            menorp = galera[p][1]
            nomep = galera[p][0]
    if escolha in 'n':
        print("--"*20)
        break
    p += 1   
    print('-=-'*20)
print(f'Foram cadastradas(as) {len(galera)} pessoa(s).')
print(f'Pessoa(s) mais pesada(s): {nome}', end='... ')
for c in galera:
    if c[0] != nome and c[1] == maiorp:
        print(f'{c[0]}', end='', sep='...')
print(f'\nPessoa(s) mais leve(s): {nomep}', end='... ')
for l in galera:
    if l[0] != nomep and l[1] == menorp:
        print(f'{l[0]}', end='', sep='... ')
print('\n*'*30)

'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''