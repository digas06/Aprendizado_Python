'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e 
fechados na ordem correta.'''
expr = input('Digite uma expressão: ')
pilha = []
for c in expr:
    if c == '(':
        pilha.append('()')
    if c == ')':
        pilha.append(')')
if pilha.count('(') == pilha.count(')'):
    print('Sue expressão é válida.')
else:
    print('Sua expressão não é válida.')   
