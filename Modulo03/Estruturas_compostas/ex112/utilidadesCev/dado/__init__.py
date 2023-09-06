'''Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. 
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), 
mas com uma validação de dados para aceitar apenas valores que seja monetários.'''


def leiaDinheiro(msg):
    while True:
        n = input(f'{msg}')
        if n.isnumeric():
            break
        if '.' in n:
            n = n.replace('.', ',')
        if ',' in n:
            n = n.replace(',', '.')
            break
        else:
            print(f'\033[31mErro! \"{n}\" não é um valor válido.\033[0m')
    return float(n)
