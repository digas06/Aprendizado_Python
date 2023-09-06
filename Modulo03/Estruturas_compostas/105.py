'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
 retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)'''


def notas(*num, sit=False):
    """
    -> Calcula situação da turma:

    -parametro num: Recebe todas as notas que vão ser calculadas
    -parametros sit=False: (opcional) Caso queira mostrar a situação da turma (sit=True)
    -return: dicionário com todas as informações (Total de notas, maior nota, menor nota, média e situação)
    """
    dic = {}
    dic['Total'] = (len(num))
    dic['Maior nota'] = max(num)
    dic['Menor nota'] = min(num)
    dic['Média da turma'] = (sum(num))/len(num)

    if sit:
        if dic['Média da turma'] < 5:
            dic['Situação'] = 'Ruim'
        elif dic['Média da turma'] >= 5 and dic['Média da turma'] < 7:
            dic['Situação'] = 'Razoável'
        else:
            dic['Situação'] = 'Boa'

    return dic


print(f'{notas()}')
