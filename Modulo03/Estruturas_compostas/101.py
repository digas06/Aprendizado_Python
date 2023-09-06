''' Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de 
nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL
 e OBRIGATÓRIO nas eleições.'''

from datetime import date


def voto(nascimento):
    idade = (date.today().year)-nascimento

    permição = ''

    if idade < 16:
        permição = 'Voto negado'

    elif idade >= 16 and idade < 18 or idade >= 70:
        permição = 'Voto Opicional'

    elif idade >= 18 and idade < 70:
        permição = 'Voto Obrigatório'

    return (f'Com {idade} o voto é: {permição}')


nasc = int(input('Data de nascimeno: '))
print(voto(nasc))