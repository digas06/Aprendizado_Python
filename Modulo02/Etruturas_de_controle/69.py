''' Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
 No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''
maior18 = homens = mulheres = 0

while True:
    idade = int(input('Idade: '))
    sexo = input('Sexo [F/M]: ').strip().lower()
    escolha = input('Deseja cntinuar? [S/N]: ').strip().lower()
    if sexo[0] in "Ff" and idade < 20:
        mulheres += 1
    if idade >= 18:
        maior18 += 1
    if sexo[0] in 'Mm':
        homens += 1
    if escolha in 'Nn':
        print("-=-"*20)
        break
    print(f'{"-=-"*20}')
print(f'Maiores de 18 anos: {maior18} pessoas.')
print(f'Homens cadastrados: {homens}')
print(f'Mulheres com menos de 20 anos: {mulheres}')

