
# Escreva um programa que solicite ao usuário para digitar seu endereço de e-mail e 
# extraia o nome de usuário (parte antes do "@") e o domínio (parte depois do "@").

email = input("Digite um email: ")

email_quebrado = email.split("@")

print(f"Nome do usuário: {email_quebrado[0]}. Domínio: {email_quebrado[1]}.")