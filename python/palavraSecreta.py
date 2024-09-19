"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
palavra_secreta = "Vinicius"
letras_certas = ""
tentativas = 0

while True:
    letra_do_usuario = str(input("Digite uma letra: "))
    tentativas += 1

    if (len(letra_do_usuario) > 1):
        print("Digite apenas uma letra!")
        continue

    if (letra_do_usuario in palavra_secreta):
        letras_certas += letra_do_usuario

    mostra_usuario = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_certas:
            mostra_usuario += letra_secreta
        else:
            mostra_usuario += "*"
    
    if (mostra_usuario == palavra_secreta):
        print(f"Você ganhou!!!\nA palavra secreta é: {palavra_secreta}\nVocê fez {tentativas} tentativas")
        break
    else:
        print(mostra_usuario)