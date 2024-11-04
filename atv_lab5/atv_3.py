
# Calculadora Simples: Faça uma calculadora que pede ao usuário dois números e uma operação (+, -, *, /) e 
# retorna o resultado dessa operação.

num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))
operacao = input("Digite uma operação (+, -, * ou /): ")

match operacao:
    case '+':
        print("Operação escolhida foi soma. Resultado:", num_1 + num_2)
    case '-':
        print("Operação escolhida foi subtração. Resultado:", num_1 - num_2)
    case '*':
        print("Operação escolhida foi multiplicação. Resultado:", num_1 * num_2)
    case '+':
        print("Operação escolhida foi divisão. Resultado:", num_1 / num_2)