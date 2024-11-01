
# Escreva um programa que solicite ao usuário para digitar seu nome e, 
# em seguida, imprima as iniciais do nome em letras maiúsculas.

nome = input("Digite seu nome completo: ").lower()

iniciais = ''

for palavra in nome.split():
    iniciais += palavra[0] + '.'

print(iniciais)