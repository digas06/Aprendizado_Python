'''Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no 
desafio 108.'''

def aumentar(n=0, aument=0, md=False):
    return n + (n * (aument / 100)) if md is False else moeda(n + (n * (aument / 100)))


def diminuir(n=0, diminui=0, md=False):
    return n - (n * (diminui / 100)) if md is False else moeda(n - (n * (diminui / 100)))


def dobro(n=0, md=False):
    return n * 2 if md is False else moeda(n * 2)


def metade(n=0, md=False):
    return n / 2 if md is False else moeda(n / 2)


def moeda(valor=0):
    formato = (f'R$ {valor:.2f}'.replace('.', ','))
    return formato
