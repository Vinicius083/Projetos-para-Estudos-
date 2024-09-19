nome = str(input('Digite seu nome: '))
quant_letras = len(nome)
count = 0
nome_asterisco = ''

while count < quant_letras:
    letra = nome[count]
    count += 1
    nome_asterisco += ('*' + letra)

print(nome_asterisco + "*")