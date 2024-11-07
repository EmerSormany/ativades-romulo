
# Conversão de Notas: Escreva um programa que converte uma nota de 0 a 100 em uma escala de conceitos: A (90-100), B (80-89), C (70-79), D (60-69) e F (0-59).

nota = int(input("Digite uma nota de 0 a 100: "))

if nota < 60:
    print("Conceito da nota F")
elif nota >= 60 and nota < 70:
    print("Conceito da nota D")
elif nota >= 70 and nota < 80:
    print("Conceito da nota C")
elif nota >= 80 and nota < 90:
    print("Conceito da nota B")
else:
    print("Conceito da nota A")