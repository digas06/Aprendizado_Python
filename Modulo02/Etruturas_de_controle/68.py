'''Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que 
ele conquistou no final do jogo. '''
from random import randint
print(f'{"-=-"*20}\n\tVamos jogar Par ou Impar\n{"-=-"*20}')
soma = contador = 0
while True:
    computador = randint(1,10)
    jogador = int(input('Escolha um número de 1 a 10: '))
    escolha = input('Par ou Ímpar? [P/I]: ').lower().strip()
    soma = computador
    soma += jogador
    print(f'Número do computador: {computador}')
    print(f'Seu número: {jogador}')
    print(f'Soma dos número: {soma}')
    if soma % 2 == 0:
        print('Deu par.')
    elif soma % 2 != 0:
        print('Deu impar.') 
    if escolha[0] in 'Pp' and soma % 2 == 0:
        print(f'Você venceu. Vamos jogar denovo:\n{"-=-"*20}')
        contador += 1
    elif escolha in 'Pp' and soma % 2 != 0:
        print(f'Você perdeu. Fim do jogo.\n{"-=-"*20}')
        break
    elif escolha[0] in 'Ii' and soma % 2 == 0:
        print(f'Você perdeu. Fim do jogo\n{"-=-"*20}')
        break
    elif escolha[0] in 'Ii' and soma % 2 != 0:
        print(f'Você venceu. Vamos jogar denovo:\n{"-=-"*20}')
        contador += 1
    else:
        print('Resposta inválida')
        break
print(f'Número de vitórias: {contador}')


