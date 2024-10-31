
# Escreva um programa que solicite ao usuário para digitar uma frase e verifique se ela contém a palavra "Python".

frase = input("Digite uma frase: ")

if frase.count("python") | frase.count("Python") | frase.count("PYTHON"):
    print("A frase possui a palavra python.")
else:
    print("A frase não possui a palavra python.")
