
# Escreva um programa que solicite ao usuário uma quantidade de horas, minutos e segundos, 
# e imprima uma mensagem formatada mostrando o total de segundos. 
# Por exemplo: "O total de segundos é {total_segundos}."

horas = int(input("Digite a quantida de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
secs = int(input("Digite a quantidade de segudos: "))

horas_sec = horas * 60 * 60
minutos_sec = minutos * 60

print(f"O total de segundos é {secs + horas_sec + minutos_sec}")