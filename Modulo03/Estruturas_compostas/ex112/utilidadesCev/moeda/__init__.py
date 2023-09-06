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


def titulo(msg):
    print('='*(40))
    print(f'{msg: ^40}')
    print('='*40)


def resumo(n=0, aument=0, diminui=0):
    dic = {f'preço analizado:': moeda(n), f'{aument}% de aumento:': aumentar(n, aument, True), 
           f'{diminui}% de desconto:': diminuir(n, diminui, True),'Dobro do valor:': dobro(n, True),
           'Metade do valor:': metade(n, True)}
    
    (titulo('RESUMO DO VALOR'))

    for chave, valor in dic.items():
        print(f'{chave:.<29} {valor: <10}')
    print('='*40)
