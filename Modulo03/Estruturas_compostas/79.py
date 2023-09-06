'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
 Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores 
 únicos digitados, em ordem crescente. '''
lista = []
while True:
    numero = int(input('Adicione um número a lista: '))
    lista += [numero]
    if lista.count(numero) > 1:
        print(f'O numero {numero} já foi adicionado. Não irei adiciona-lo.')
        lista.remove(numero)
    else:
        print(f'Número {numero} adicionado com sucesso.')
    escolha = input('Quer continuar? [S/N]: ').lower().strip()
    if escolha in 'Nn':
        break

lista.sort()
print(f'Valores adicionados: ', end='')
for c in lista:
    print(f'{c}', sep=' ', end=' ')
