'''Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da
 digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma 
 funcionalidade.'''


def leiaInt(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            return (f'Número digitado: {numero}')
        except ValueError:
            print(f'ERRO: digite um inteir válido.')
            continue
        except KeyboardInterrupt:
            print('O usuário preferil não digitar este número')
            return (f'Valor digitado: 0')


def leiaFloat(msg):
    while True:
        try:
            numero = float(input(msg))
            return (f'Número digitado: {numero}')
        except (ValueError, TypeError):
            print('Erro: Digite um valor real válido.')
        except (KeyboardInterrupt):
            return (f'O usuário preferil não digitar este número')

print(leiaInt('Digite um número inteiro: '))
print(leiaFloat('Digite um número real: '))
