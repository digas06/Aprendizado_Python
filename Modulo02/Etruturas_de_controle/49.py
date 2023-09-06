'''Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
 só que agora utilizando um laço for.'''
n = int(input('digite um número: '))
for c in range(1,11):
    print(f'{n} X {c:2} = {n*c:2}')