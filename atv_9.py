# Escreva um programa que solicite ao usuário dois valores booleanos (True ou False) e armazene-os em variáveis. 
# Em seguida, aplique os operadores lógicos "and", "or" e "not" entre essas variáveis e imprima os resultados.

verdadeiro = input("Digite 'true' para valor verdadeiro: ")
falso = input("Digite 'false' para o valor falso: ")

verdadeiro_upado = verdadeiro.upper()
falso_upado = falso.upper()

verdadeiro_bool:bool
falso_bool:bool

if(verdadeiro_upado == "TRUE"):
    verdadeiro_bool = True

if(falso_upado):
    falso_bool = False

print(" resultado do operador 'and' comparando os 2 valores:", verdadeiro_bool and falso_bool, "\n", "resultado do operador 'or' comparando os 2 valores:", 
      verdadeiro_bool or falso_bool, "\n", 
      "resultado do operador 'not' negando os 2 valores:", not verdadeiro_bool, not falso_bool)