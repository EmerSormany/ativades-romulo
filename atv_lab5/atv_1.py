
# Escreva um programa que solicita um número ao usuário e determina se é positivo, negativo ou zero.

num = int(input("Digite um número: "))


match num:
    case x if x < 0:
        print("Negativo")
    case x if x > 0:
        print("Positivo")
    case _:
        print("Neutro")
