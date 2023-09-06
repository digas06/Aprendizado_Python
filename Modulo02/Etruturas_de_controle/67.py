''' Faça um programa que mostre a tabuada de vários números, um de cada vez, 
para cada valor digitado pelo usuário. O programa será interrompido quando o número 
solicitado for negativo. '''
while True:
    numero = int(input('Quer ver a tabuada de qual número? '))
    if numero < 0:
        break
    for c in range(1,11):
        print(f'{numero:2} X {c:2} = {numero * c}')
print('Programa de tabuada encerrado. Volte sempre.')