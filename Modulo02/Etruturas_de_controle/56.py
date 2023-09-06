'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
 No final do programa, mostre: a média de idade do grupo,
 qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
somador = 0
mais_velho_idade = 0
nome_v = 0
cont = 0
for c in range(1, 5):
    print(f'{"=":=^10} {c}° PESSOA {"=":=^10}')
    nome = input(f'Nome: ').strip().lower()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').lower().strip()
    somador += idade
    if c == 1 and sexo[0] == 'm':
        mais_velho_idade = idade
        nome_v = nome
    if sexo[0] == 'm' and idade > mais_velho_idade:
        nome_v = nome
        mais_velho_idade = idade
    if sexo [0] == 'f' and idade < 20:
        cont += 1
print(f'Média de idades: {somador / 4}\nHomem mais velho: {nome_v.title()}\nMulheres com menos de 20: {cont}')
