
# Escreva um programa que solicite ao usuário seu nome completo e imprima as iniciais de cada palavra em letras maiúsculas. 
# Por exemplo, se o nome for "Fulano de Tal", o programa deve imprimir "F.D.T."

nome = input("Digite um texto: ")

nome_quebrado = nome.split(" ")

inicais = ''

for palavra in nome_quebrado:
    inicais = inicais + palavra[0].upper() + '.'

print(inicais)