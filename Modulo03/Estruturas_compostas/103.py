'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do
jogador, mesmo que algum dado não tenha sido informado corretamente.'''


def ficha(n=0, g=0):
    if n:
        n = n
    else:
        n = '<desconhecido>'
    if g.isnumeric():
        g = int(g)
    else:
        g = 0
    return (f'O jogador {n} fez {g} gols.')


print(ficha(input('Nome: '), str(input('Número de gols: '))))
