'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''
lista = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    escolha = input('Quer continuar? [S/N]: ').lower().strip()
    if escolha in 'n':
        break
print(f'Foram digitados: {len(lista)}')
lista.sort(reverse=True)
print(f'Em ordem decresente: {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista.')
else:
    print(f'O valor 5 não faz parte da lista.')