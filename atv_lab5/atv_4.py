
# Maior de Três Números: Escreva um programa que solicita três números ao usuário e retorna o maior dentre eles.

num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))
num_3 = int(input("Digite o terceiro número: "))

if num_1 > num_2 and num_1 > num_3:
    print(f'{num_1} é o maior dos números!')
elif num_2 > num_1 and num_2 > num_3:
    print(f'{num_2} é o maior dos números!')
else:
    print(f'{num_3} é o maior dos números!')