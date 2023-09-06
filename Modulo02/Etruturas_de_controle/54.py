'''Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
ordem = 1
maior = 0
menor = 0
for c in range(1, 8):
    pessoa = int(input(f'{ordem}° pessoa: '))
    ordem += 1
    if pessoa >= 18:
        maior += 1
    elif pessoa < 18:
        menor += 1
print(f'Maiores de idade: {maior}\nMenor idade: {menor}')