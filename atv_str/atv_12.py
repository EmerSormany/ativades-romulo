
# Escreva um programa que solicite ao usuário uma frase e 
# imprima uma mensagem formatada mostrando a quantidade de caracteres, palavras e linhas na frase.

frase = input("Digite uma frase: ")
frase_quebrada = frase.split(" ")

qtd_caracteres = len(frase)
qtd_palavras = len(frase_quebrada)
qtd_de_linhas = len(frase.splitlines())

print(f'quantidade de caracteres: {qtd_caracteres}. Quantidade de palavras: {qtd_palavras}. Quantidade de palavras: {qtd_de_linhas}.')
