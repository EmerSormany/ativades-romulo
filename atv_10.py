# Escreva um programa que solicite ao usuário duas strings e verifique se elas são iguais. Imprima uma mensagem informando o resultado da comparação.

text_1 = input("Digite algum texto: ")
text_2 = input("Digie algum texto: ")

if(text_1.upper() == text_2.upper()):
    print("Textos são iguais!")
else:
    print("Textos não são iguais!")