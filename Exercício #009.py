#009 – Tabuada
#Faça um programa um número inteiro qualquer e mostre na tela sua tabuada.
num = int(input('Digite um número para calcular a tabuada: '))
cont = 1
while cont<=10:
  tab = num*cont
  print(num, "x", cont,"=",tab)
  cont = cont + 1