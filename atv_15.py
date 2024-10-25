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

dia_em_secs = dia * 60 * 60 * 24 * 1000
mes_em_secs = mes * dia
ano_em_secs = ano * mes_em_secs

print(dia_em_secs + mes_em_secs + ano_em_secs)