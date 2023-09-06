'''Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", 
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''
frase = str(input('Digite uma frase: ')).strip().lower()
print(f'Número de "A": {frase.count("a")}\nPrimeia letra "A": {frase.find("a")}\nÚltima letra "A": {frase.find("a", -1)}')
