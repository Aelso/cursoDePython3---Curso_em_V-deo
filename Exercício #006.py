#006 - Dobro, Triplo, Raiz Quadrada
#Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e a sua raiz quadrada.
import math
num = float(input('Digite um número: '))
dob = num*2
tri = num*3
rq = math.sqrt(num)
print('O dobro é {}\nO triplo é {}'.format(dob,tri))
print('A raiz quadrada:{}'.format(rq))