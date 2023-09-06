'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
o primeiro que indique o número a calcular e outro chamado show, que será um valor 
lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''


def fatorial(n=0, show=False):
    """
        -> Calcula fatorial:
    -parametro n: Número a ser calculado
    -parametro show=False: (Opcional), caso queria mostar o calculo -- show=True
    """
    fac = 1
    print(f'{n}! = ', end='')
    for c in range(n, 0, -1):
        fac *= c
        if show:
            if c != 1:
                print(f'{c}', end=' -> ', sep=' = ')
            else:
                print(f'{c}', end=' = ')
    return (f'{fac}')


numero = int(input('Número: '))

print(f'{fatorial(numero)}')
