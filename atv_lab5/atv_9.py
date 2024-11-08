
# Calculadora de IMC: Peça ao usuário seu peso e altura e calcule o índice de massa corporal (IMC). 
# Em seguida, mostre uma mensagem indicando se a pessoa está abaixo do peso, com peso normal, com sobrepeso, obesa ou muito obesa.

peso = float(input("Digite o peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura**2)

if imc < 18.5:
    print("Está abaixo do peso.")
elif imc >= 18.5 and imc < 25:
    print("Está and peso ideal.")
elif imc >= 25 and imc < 30:
    print("Está com sobrepeso.")
elif imc >= 30 or imc < 35:
    print("Está obeso.")
else:
    print("Está muito obeso.")