
# Escreva um programa que solicite ao usuário dois números e imprima uma mensagem formatada mostrando a soma, 
# subtração, multiplicação e divisão dos números. Por exemplo: "A soma de {num1} e {num2} é {soma}."

num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))

print(f'A soma de {num_1} e {num_2} é {num_1 + num_2}.')
print(f'A subtração de {num_1} e {num_2} é {num_1 - num_2}.')
print(f'A multiplicação de {num_1} e {num_2} é {num_1 * num_2}.')
print(f'A divisão de {num_1} e {num_2} é {num_1 / num_2}.')
