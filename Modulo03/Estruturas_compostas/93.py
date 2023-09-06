'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do 
jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
dic = {
    'Nome': input('Nome do jogador: ').strip().title(),
    'Partidas':  int(input('Partidas jogadas: '))
}
if dic['Partidas'] > 0:
    dic['Gols'] = []
    for c in range(dic['Partidas']):
        dic['Gols'].append(int(input(f'  Número de gols na {c+1} partidas: ')))
print('-='*20)
print(f'{dic}\n{"-="*20}')
for chave, valor in dic.items():
    print(f'{chave}: {valor}')
print('-='*20)
print(f'Jogador: {dic["Nome"]}\nPartidas jogadas: {dic["Partidas"]}')
print('-'*30)
if dic['Partidas'] > 0:
    for c in range(dic['Partidas']):
        print(f'Partida: {c+1} => {dic["Gols"][c]} gols')
