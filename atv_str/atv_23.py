
# Escreva um programa que solicite ao usuário para digitar uma frase 
# e verifique se todas as palavras estão em letras maiúscula.

frase = input("Digite uma frase: ")

if frase == frase.lower():
    print("Todas as letras são minúsculas.")
else:
    print("Nem todas as letras são minúsculas")