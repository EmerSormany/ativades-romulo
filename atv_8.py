

# Escreva um programa que solicite ao usuário um número e verifique se ele é par ou ímpar. Imprima uma mensagem informando o resultado.

num = int(input('Digite um número: '))

div = num % 2

if div != 0:{
    print("O número é ímpar")
}
else:{
    print("O número é par")
}
