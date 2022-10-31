#007 - Média Aritmética
#Desenvolver um programa que leia as duas notas do aluno, calcule e mostre sua média.
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2 
print('a nota 1 foi {}\ne a nota 2 foi {}'.format(nota1, nota2))
print('A média final:{}'.format(media))