'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro 
e mostre uma mensagem com tamanho adaptável.

Ex: 
escreva('Olá, Mundo!')
Saída:
~~~~~~~~~
Olá, Mundo!
~~~~~~~~~
'''


def escreva(título):
    tam = len(título)
    print(f'{"-"*(tam+4):^}\n  {título:^}  \n{"-"*(tam+4):^}')


escreva('Teste de título')
print()
escreva('Outro teste')
print()
escreva('Olá')
print()
escreva('Este é um teste com um texto maior')
