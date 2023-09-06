''' Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, 
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
escritos = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'douze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
              'dezenove', 'vinte')
numero = int(input('Número de 0 a 20: '))
while True:
    while numero < 1 or numero > 20:
        numero = int(input('Opção inválida. Digite um número de 0 a 20: '))
    print(f'Número por extenso: {escritos[numero-1].title()}')
    break
    