# Escreva um programa que solicite ao usuário dois números inteiros e armazene-os em variáveis. 
# Em seguida, calcule e imprima a soma, subtração, multiplicação e divisão desses números.

num_1 = int(input('Digite um número: '))
num_2 = int(input('Digite outro número: '))

soma = num_1 + num_2
sub = num_1 - num_2
div = num_1 / num_2
mult = num_1 * num_2

print('Soma:', soma)
print('Subtração:', sub)
print('Divisão:', div)
print('Multiplicação:', mult)