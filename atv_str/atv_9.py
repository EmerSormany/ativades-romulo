
# Escreva um programa que solicite ao usuário uma frase e substitua todas as vogais por asteriscos (*). 
# Em seguida, imprima a frase formatada.

frase = input("Digite uma frase: ")

frase_formatada = frase.replace('a', '*')
frase_formatada = frase_formatada.replace('e', '*')
frase_formatada = frase_formatada.replace('i', '*')
frase_formatada = frase_formatada.replace('o', '*')
frase_formatada = frase_formatada.replace('u', '*')

# frase_formatada_e = frase_formatada_a.replace('e', '*')
# frase_formatada_i = frase_formatada_e.replace('i', '*')
# frase_formatada_o = frase_formatada_i.replace('o', '*')
# frase_formatada_u = frase_formatada_o.replace('u', '*')

print(frase_formatada)