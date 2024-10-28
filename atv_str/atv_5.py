
# Escreva um programa que verifique se uma palavra é um palíndromo (lê-se igual de trás para frente). Exemplo: "radar".

palavra = input("Digite um palavra: ")

if(palavra == palavra[::-1]):
    print("Palavra é uma políndromo")
else:
    print("Não é um políndromo")