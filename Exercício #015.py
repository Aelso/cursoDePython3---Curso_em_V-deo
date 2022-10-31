#015 - Aluguel de Carros
#Escreva um programa que pergunte a quantidade de quilômetros percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa 60 reais por dia e 15 centavos por quilômetro rodado.
quantKm = float(input('Quanto quilômetros percorridos até agora?'))
quantDia  = int(input('Quantidade dias que carro foi a um alugado?'))
calPerc = (quantKm * 0.15) + (quantDia * 60)
print('O total a pagar para empresa de locação de veículos é R$ {}'.format(calPerc))