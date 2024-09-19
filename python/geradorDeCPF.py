import random

cpf = ""
multiplicador = 10
soma = 0

for i in range(9):
    cpf += str(random.randint(0, 9))

while multiplicador > 1:
    for numero in cpf:
        multiplicacao = int(numero) * multiplicador
        soma += multiplicacao
        multiplicador -= 1

segunda_multiplicacao = soma * 10
resto_da_2divisao = segunda_multiplicacao % 11
primeiro_numero = 0 if resto_da_2divisao > 9 else resto_da_2divisao

cpf = cpf + str(primeiro_numero)
multiplicador = 11
soma = 0

while multiplicador > 1:
    for numero in cpf:
        multiplicacao = int(numero) * multiplicador
        soma += multiplicacao
        multiplicador -= 1

terceira_multiplicacao = soma * 10
resto_da_3divisao = terceira_multiplicacao % 11
segundo_numero = 0 if resto_da_3divisao > 9 else resto_da_3divisao


cpf += str(segundo_numero)
cpf = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])

print(cpf)

