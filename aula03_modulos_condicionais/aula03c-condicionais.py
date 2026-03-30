#ESTRUTURA CONDICIONAL SIMPLES
media = 6
nota = ()

b1 = float(input("Digite sua nota: "))
b2 = float(input("Digite sua nota: "))
b3 = float(input("Digite sua nota: "))
b4 = float(input("Digite sua nota: "))

soma = (b1 + b2 + b3 + b4)
media_final = soma / 4

if media_final <6:
    print(f"Reprovado com: {media_final}")

else:
    print(f"Aprovado com: {media_final}")


# Verificação

verifica_email = True
verifica_senha = True

verifica_login = verifica_email and verifica_senha
print (verifica_login)

if verifica_login:
    print("Entra no programa... Executa...")

# ou
logica_ou = False or False or False
print(logica_ou)

# negação
negacao = not false
print(negacao)

if not verifica_login:
    print("Logando...")