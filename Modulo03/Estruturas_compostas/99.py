''' Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores 
inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''


def maior(*num):
    from time import sleep
    maior = 0
    for c in num:
        print(f'{c}', end=' ')
        sleep(0.5)
    for c in range(len(num)):
        if c == 0:
            maior = num[c]
        else:
            if num[c] > maior:
                maior = num[c]
    print(f'\nForam digitados {len(num)} valores.\nMaior valor: {maior}')


maior()
