'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''
palavras = ('Abacaxi', 'Aconchegante', 'Esmeralda',
            'Trampolim', 'Efervescente')
for palavra in palavras:
    print(f'\nNa palavra {palavra} temos: ', end='')
    for letra in palavra:
        if letra.lower() in 'aáàâãeéiíoóõôuó':
            print(f'{letra.lower()}', end=' ')
