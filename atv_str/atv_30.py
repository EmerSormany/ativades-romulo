
# Escreva um código que capitalize a primeira letra de cada palavra em uma frase. 
# Exemplo: "python é incrível" deve se tornar "Python É Incrível".

texto = input("Digite um texto: ")

txt_formatado = ''

for x in texto.split():
    txt_formatado += x[0].upper() + x[1:].lower() + ' '

print(txt_formatado)