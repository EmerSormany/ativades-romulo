# Escreva um programa que solicite ao usuário para digitar seu nome em letras minúsculas e, em seguida, imprima o nome com a primeira letra em maiúscula.

nome = input("Digite seu nome com letras minúsculas: ")

nome_quebrado = nome.split()

nome_formatado = ''

for x in nome_quebrado:
    nome_formatado += x[0].upper() + x[1:] + ' '


print(nome_formatado)