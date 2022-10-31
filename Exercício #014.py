#014 - Conversor de Temperaturas
#Escreva um programa de converter uma temperatura digitada em °C e converta para °F.
tempC = float(input('Digite a temperatura é °C: '))
tempFa = 1.8 * tempC + 32
print('A temperatura em Celsius é {} corresponde a {}°F'.format(tempC, tempFa))