'''Crie um código em Python que teste se o site pudim está acessível pelo computador usado.'''
import urllib.request

try:
    open = urllib.request.urlopen('http://www.pudim.com.br')

except urllib.error.URLError:
    print('Não foi possível abrir o site.')
else:
    print('O site está funcionando')
    print(f'{open.read()}')
