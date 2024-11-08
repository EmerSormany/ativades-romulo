
# Verificação de Triângulo: Peça ao usuário o comprimento de três lados e verifique se eles podem formar um triângulo. 
# Se sim, determine se é um triângulo equilátero, isósceles ou escaleno.

medida_1 = int(input("DIgite a primeira medida: "))
medida_2 = int(input("DIgite a segunda medida: "))
medida_3 = int(input("DIgite a terceira medida: "))

if medida_1 + medida_2 < medida_3 or medida_1 + medida_3 < medida_2 or medida_3 + medida_2 < medida_1:
    print("As medidas não formam um triângulo.")
else:
    if medida_1 == medida_2 and medida_1 == medida_3:
        print("O triângulo é equilátero.")
    elif medida_1 == medida_2 and medida_1 != medida_3 or medida_2 == medida_3 and medida_2 != medida_1 or medida_3 == medida_1 and medida_3 != medida_2:
        print("O triângulo é isóceles.")
    else:
        print("O triângulo é escaleno.")