'''Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização
 de detalhes do aproveitamento de cada jogador.

Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do 
jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.  
'''
lista = []
while True:
    dic = {
        'Nome': input('Nome: ').strip().title(),
        'Partidas': int(input('Partidas jogadas: '))
    }
    if dic['Partidas'] > 0:
        dic['Gols'] = []
        for c in range(dic['Partidas']):
            dic["Gols"].append(int(input(f'\tGols na {c+1}ª partida: ')))
            dic['Soma']= sum(dic['Gols'])
    lista.append(dic.copy())
    escolha = input('Quer continuar? [S/N]: ').strip().lower()
    while escolha[0] not in 'sn':
        escolha = input('Resposta inváida. Quer continuar? [S/N]: ')
    if escolha[0] in 'n':
        break
print('-='*20)
print(f'\tDados do time\t\n{"-="*20}')
print(f'{"Nº":<5}{"Nome":<10}{"Gols":<15}{"TOTAL"}')
print('--'*20)
for pos, c in enumerate(lista):
    print(f'{pos:<5}{c["Nome"]:<10}{c["Gols"]} \t{c["Soma"]}')
print('-='*20)
while True:
    escolha = int(input('Quer consultar os dados de qual jogador? (999)interrompe: '))
    print('--'*20)
    if escolha == 999:
        break
    print(f'Levantamento do jogador {lista[escolha]["Nome"]}')
    a = 0
    for gol in lista[escolha]["Gols"]:
        print(f'{a+1}º jogo ==> {gol} gols.')
        a += 1
    print('-='*20)
