"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
#PRIMEIRO DIGITO
cpf = str(input("Digite seu cpf no formato [000.000.000-00]: "))
parte1, parte2, parte3 = cpf.split(".")
parte3, vericadores = parte3.split("-")

cpf = parte1 + parte2 + parte3
multiplicador = 10
soma = 0

while multiplicador > 1:
    for numero in cpf:
        multiplicacao = int(numero) * multiplicador
        soma += multiplicacao
        multiplicador -= 1

segunda_multiplicacao = soma * 10
resto_da_2divisao = segunda_multiplicacao % 11
primeiro_numero = 0 if resto_da_2divisao > 9 else resto_da_2divisao

#SEGUNDO DIGITO
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

digitos_confirmadores = str(primeiro_numero) + str(segundo_numero)

#VERIFICAÇÃO
if (digitos_confirmadores == vericadores): 
    print("Parabéns, seu CPF é valido!")
else:
    print("CPF invalido")