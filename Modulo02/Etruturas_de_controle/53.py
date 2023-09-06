'''Crie um programa que leia uma frase qualquer e
 diga se ela é um palíndromo, desconsiderando os espaços.'''
f = input('Frase: ').strip().lower()
f = ''.join(f.split(' '))
diminuidor = len(f)-1
a = ''
for c in f:
    a += f[diminuidor]
    diminuidor -= 1
if f == a:
    print(f'Plavara ao contrário: {a}\nÉ um palíndromo')
else:
    print('Não é um palíndromo.')
    
