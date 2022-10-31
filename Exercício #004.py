#004 - Dissecando uma Variável
#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo 
# e todas as informações possíveis sobre eles.
verik = input('Digite algo no Teclado:')
print('O tipo primitivo {} '.format(type(verik)))
print('Só tem espaço? {}: '.format(verik.isspace()))
print('É númerico?{}: '.format(verik.isalnum()))
print('E alfabetico?{}: '.format(verik.isalpha()))
print('É alfanúmerico?{}: '.format(verik.isalnum()))
print('Está em Maiúsculas? {}: '.format(verik.isupper()))
print('Está em minúsculas? {}: '.format(verik.islower()))
print('Está Capitalizado? {}: '.format(verik.istitle()))