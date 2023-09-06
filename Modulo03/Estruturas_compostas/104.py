'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 
'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')'''
def leiaInt(msg):
    while True:
        numero = str(input(msg))
        if numero.isnumeric():
            return int(numero)
        else:
            print('\033[31mERRO. Digite um número válido!\033[0m')
    

n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')