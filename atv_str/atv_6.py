
# Escreva um programa que remova todos os espaços em branco de uma string.

palavra = "OI, meu nome é Sormany"

junto = palavra.split(" ")

sem_espaco = ''

for x in junto:
    sem_espaco = sem_espaco+x

print(sem_espaco)