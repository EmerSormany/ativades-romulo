
# Classificação de Idade: Peça a idade do usuário e classifique-a em 
# "Criança" (0-12), "Adolescente" (13-19), "Adulto" (20-59) ou "Idoso" (60+).

idade = int(input("Digite sua idade: "))

if idade >= 60:
    print("Idoso")
elif idade < 60 and idade >= 20:
    print("Adulto")
elif idade < 20 and idade >= 13:
    print("Adolescente")
else:
    print("Criança")