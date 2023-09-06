''' Adapte o código do desafio #107, criando uma função adicional chamada moeda() 
que consiga mostrar os números como um valor monetário formatado.'''


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


def moeda(valor=0):
    formato = (f'R$ {valor:.2f}'.replace('.', ','))
    return formato