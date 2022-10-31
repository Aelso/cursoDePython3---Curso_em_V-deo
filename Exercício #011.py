#011 - Pintando Parede
#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área 
# e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta, pinta uma área de 2m2
alt = float(input('Digite a altura: '))
larg = float(input('Digite a largura: '))
area = alt*larg
tint = (alt*larg)/2
print('A área em metros quadrado é',area,'e a quantidade de tinta necessária é',tint,'litro(s) de tinta')