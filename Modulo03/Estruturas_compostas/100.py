'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
a soma entre todos os valores pares sorteados pela função anterior.'''
from random import randint


def sorteia(lista):
    while len(lista) < (5):
        num = randint(1, 10)
        if num not in lista:
            lista.append(num)
    print(f'Números sorteados: {lista}')


def somaPar(lista):
    somador = 0
    for c in lista:
        if c % 2 == 0:
            somador += c
    print(f'A soma dos números pares é {somador}.')


numeros = []
sorteia(numeros)
somaPar(numeros)
