#012 - Calculando Descontos
#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
preco = float(input('Digite o preço do produto: '))
desc = preco * 0.95
print('O preço do produto é R$ {} e com desconto fica R$ {:.2f}'.format(preco, desc))