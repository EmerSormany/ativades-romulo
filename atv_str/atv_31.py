
# Escreva um programa para ler uma frase, imprima esta frase com as palavras ordenadas
# em ordem crescente de comprimento das strings.

frase = input("Digite uma frase: ")

palavras = frase.split()

palavras_ordenadas = sorted(palavras, key=len)

print(' '.join(palavras_ordenadas))
