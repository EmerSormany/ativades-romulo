
# Conversão de Notas: Escreva um programa que converte uma nota de 0 a 100 em uma escala de conceitos: A (90-100), B (80-89), C (70-79), D (60-69) e F (0-59).

nota = int(input("Digite uma nota de 0 a 100: "))

if nota in list(range(60)):
    print("Conceito da nota F")
elif nota in list(range(60, 70)):
    print("Conceito da nota D")
elif nota in list(range(70, 80)):
    print("Conceito da nota C")
elif nota in list(range(80, 90)):
    print("Conceito da nota B")
elif nota in list(range(90, 101)):
    print("Conceito da nota A")
else:
    print("Nota inválida.")