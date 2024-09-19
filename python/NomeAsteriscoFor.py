nome = str(input("Digite seu nome: "))
novo_nome = ""

for letra in nome:
    novo_nome += f"{letra}" + "*"
print("*" + novo_nome)