'''Crie um programa que leia vários números inteiros pelo teclado.
 O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
 No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''
print('Para parar o programa digite 999')
somador = 0
while True:
    n = int(input('Número inteiro: '))
    if n == 999:
        break
    somador += n
print(f'A soma de todos os valores é: {somador}')