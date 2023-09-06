'''Faça um programa que leia o peso de cinco pessoas.
 No final, mostre qual foi o maior e o menor peso lidos.'''
maior = 0
for c in range(1, 6):
    peso = float(input(f'Peso da {c}° pessoa: '))
    if peso > maior:
        maior = peso
    if c == 1:
        menor = peso
    if peso < menor:
            menor = peso
print(f'Maior peso: {maior}kg\nMenor peso: {menor}Kg')