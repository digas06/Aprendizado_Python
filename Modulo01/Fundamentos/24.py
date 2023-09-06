'''Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".'''

cidade = input('Digite o nome de uma cidade: ').strip().lower()
primeira = cidade.split()
print(f'Começa com o nome "Santo": {primeira[0]=="santo"}')
