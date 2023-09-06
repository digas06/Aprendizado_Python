'''Crie um programa que leia duas notas de um aluno e calcule sua média, 
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = ((n1 + n2)/2)
print(f'Média: {media}')
if media < 5.0:
    print('\033[31mREPROVADO!\33[0m')
elif media >= 7:
    print('\033[32mAPROVADO!\033[0m')
else:
    print('\033[33mRECUPERAÇÃO!\033[0m')