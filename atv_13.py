# Escreva um programa em Python que solicite ao usuário dois números inteiros e troque os valores das variáveis. Em seguida, imprima os valores atualizados.


num_1 = input("Digite um número: ")
num_2 = input("Digite outro número: ")
print("Valores antes da troca, numero 1 =", num_1, "e número 2 =", num_2)
num = num_2
num_2 = num_1
num_1 = num
print("Valores depois da troca, numero 1 =", num_1, "e número 2 =", num_2)