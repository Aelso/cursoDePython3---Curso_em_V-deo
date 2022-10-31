#Crie script python que leia o nome de uma pessoa e mostre uma mensagem de boas vindas de acordo com o valor digitado.
nome = input('Qual é seu nome ? ')
print('Olá!',nome,',Prazer em te conhecer!')

# Versão colorida
nome = input('\033[4;33mQual é seu nome:\033[m?')
print('\033[1;35;41mOlá\033[m,\033[4;32;43m{}\033[m\033[4;33;40mPrazer em te conhecer!\033[m'.format(nome))
