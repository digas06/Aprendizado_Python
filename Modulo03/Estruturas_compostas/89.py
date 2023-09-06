'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
 de cada aluno individualmente.'''
lista = []
lista_temp = []
cont = 0
while True:
    lista_temp.append(input('Nome: ').strip())
    lista_temp.append(float(input('Nota 1: ')))
    lista_temp.append(float(input('Nota 2: ')))
    lista.append(lista_temp[:])
    lista_temp.clear()
    escolha = input('Quer continuar? [S/N]: ').lower().strip()
    lista[cont].append((lista[cont][1]+lista[cont][2])/2)
    cont += 1
    if escolha in 'Nn':
        cont = 0
        print("-="*25)
        print(f'{"N°": <5}{"Nome": <10}{"Média": <10}\n{"-"*30}')
        while cont <= len(lista)-1:
            print(f'{cont: <5}{lista[cont][0]: <10}{lista[cont][3]:<10.1f}')
            cont += 1 
        break
print("-="*25)
while True:
    aluno = int(input('Mostrar nota de qual aluno? (999 para parar): '))
    if aluno == 999:
        print("-="*30)
        break
    print(f'O aluno {lista[aluno][0]} tirou {lista[aluno][1:3]}.')
    print("-="*30)
