'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), 
dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.'''

def aumentar(n=0, aument=0):
    return n + (n * (aument / 100)) 


def diminuir(n=0, diminui=0, md=False):
    return n - (n * (diminui / 100)) 


def dobro(n=0, md=False):
    return n * 2 


def metade(n=0, md=False):
    return n / 2 


def titulo(msg):
    print('='*(40))
    print(f'{msg: ^40}')
    print('='*40)

