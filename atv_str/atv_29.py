
# Escreva um programa que peça ao usuário para digitar seu nome completo e, em seguida, imprima apenas o sobrenome.

nome = input("Digite seu nome completo: ")

print(nome.split()[len(nome.split())-1])