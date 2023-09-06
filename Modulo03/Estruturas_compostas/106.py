'''Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o 
manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante:
use cores.'''
from time import sleep

cores = [
    '\033[0m',           # 0 Sem cores
    '\033[0;30;41m',    # 1 vermelho
    '\033[0;30;42m',    # 2 Verde
    '\033[0;30;43m',    # 3 Amarelo
    '\033[0;30;44m',    # 4 Azul
    '\033[0;30;45m',    # 5 Roxo
    '\033[0;30;46m',    # 6 Azul-claro
    '\033[0;30;47m',    # 7 Cinza
    '\033[7;30m'        # 8 branco
]


def titulo(msg, cor=0):
    print(f'{cores[cor]}', end='')
    print(f'{"~"*(len(msg)+4)}')
    print(f'  {msg: ^}  ')
    print(f'{"~"*(len(msg)+4)}')
    
    print('\033[0m')
    sleep(1)


def comando(cmd, cor = 0):
  titulo(f'Acessando documentos do comando {cmd}', 7)
  sleep(2)
  print(f'{cores[cor]}')
  print(f'{help(cmd)}')
  print(f'\033[0m')


titulo('Sistema de ajuda PyHelp', 2)

c = ''
while True:
    c = input('Função biblioteca: ').strip().lower()
    if c == 'fim':
       break
    comando(c, 6)
    
