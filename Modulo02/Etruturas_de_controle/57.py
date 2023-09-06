'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''
sexo = input('Sexo [M/F]: ').lower().strip()
while sexo[0] not in 'FfMm':
    sexo = input('Opção inválida. Digite o sexo novamente [M/F]: ')
    if sexo[0] == 'f' or sexo[0] == 'm':
        break
print('Sexo cadastrado com sucesso.')
