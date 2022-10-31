#010 - Conversor de Moedas.
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. 
#Considere o dólar: US$1.00 = 3.27.
dol = float(input('Digite a cotação do Dólar no dia hoje: '))
diReal = float(input('Digite quanto valor em R$ você possui: '))
convDol = diReal/dol
print('Cotação do Dólar é US$ {} e você possui R$ {}\nConvertido US$ {:.2f}'.format(dol, diReal, convDol))