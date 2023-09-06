'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''
valores = (int(input('Digite um valor: ')),
           int(input('Digite outro valor: ')),
           int(input('Digite outro valor: ')),
           int(input('Digite outro valor: ')))
print(f'O 9 apareceu {valores.count(9)} vezes.')
for c in valores:
    if c == 3:
        print(f'Primeiro três: {valores.index(3)+1}° posição')
    if c % 2 == 0:
        print(f'Foram pares: {c} números')

