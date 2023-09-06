'''Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário
 digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e
   qual foi a soma entre elas (desconsiderando o flag).'''
contador = somador = 0
print('Para parar digite "999"')
while True:  
    numero = int(input('Número: '))
    if numero == 999:
        break
    somador += numero
    contador += 1
print(f'Fora digitados: {contador} números\nSoma de todos eles eles: {somador}')