''' Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
 O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
maior = menor = numero = 0

while True:
    print('Para fechar o programa digite: [ F ]')
    if numero != 'F' or numero != 'F':
        numero = int(input('Digite um número: '))
        maior = numero
        menor = numero
    numero = int(input('Digite outro número: '))
    escolha = input('Deseja continuar? [S/N]: ')
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    if escolha[0] in 'Nn':
        break
    while escolha in 'Ss':
        numero = int(input('Digite outro número: '))
        escolha = input('Deseja continuar? [S/N]: ')
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    break    
print('Programa encerrado')
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')
