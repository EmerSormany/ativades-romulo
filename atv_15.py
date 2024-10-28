# Escreva um programa que dado um dia, mes e ano calcule o valor em termos de UNIX Epoch﻿ Time (o número de milessegundos desde 00:00 de 01 de Janeiro de 1970).
# a) Considere que todos os anos possuem 365 dias
# b) Considere os anos bissextos

# 1 ano = 365 dias
# 1 dia = 24 h
# 1 h = 60 min
# 1 min = 60 seg

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mes: "))
ano = int(input("Digite o ano: "))

dia_msec = dia * 24 * 60 * 60 * 1000
mes_msec = mes * 30 * 24 * 60 * 60 * 1000
ano_msec = (ano - 1970) * 12 * 30 * 24 * 60 * 60 * 1000

print(dia_msec + mes_msec + ano_msec)

# Exercício incompleto