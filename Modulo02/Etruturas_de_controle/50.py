'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
Se o valor digitado for ímpar, desconsidere-o.'''
soma = 0
for c in range(1, 7):
    numero = int(input(f'{c}° número: '))
    if numero % 2 == 0:
        soma += numero
print(f'A soma dos números pares é: {soma}')