#008 - Conversor de Medidas
#Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros.
met = float(input('Digite o valor em metros: '))
cent = met/100
mili = met/1000
print('O valor em centímetros é {}\ne em milímetros é {}'.format(cent,mili))