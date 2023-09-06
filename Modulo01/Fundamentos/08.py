''' Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.'''
m = float(input('Valor em metro: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m / 0.1
cm = m / 0.01
mm = m / 0.001

print(f'Em quilômetro: {km}km\nEm hequitômetro: {hm}hm\nEm decâmetro: {dm}dm\nEm metros: {m}m\nEm decímetro: {dm}dm\nEm centímetros: {cm}cm\nEm milímetros: {mm}mm')
