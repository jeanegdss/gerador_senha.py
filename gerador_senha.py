import random
import string

print("GERADOR DE SENHAS")

tamanho = int(input("Quantos caracteres a senha deve ter? "))

caracteres = string.ascii_letters + string.digits + string.punctuation

senha = ""

for i in range(tamanho):
    senha += random.choice(caracteres)

print("Senha gerada:", senha)
