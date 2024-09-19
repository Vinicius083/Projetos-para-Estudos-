lista_de_compras = [];

while True:
    input_usuario = str(input(f"Digite o que deseja fazer:\n[I]nserir | [D]eletar | [L]istar: "));

    if (input_usuario.lower() == "i"):
        adicao = str(input("Digite o que deseja adicionar a sua lista: "));
        lista_de_compras.append(adicao);
        for indice, item in enumerate(lista_de_compras):
            print(indice, item);
    
    elif (input_usuario.lower() == "d"):
        deletar = int(input("Digite o indice do que deseja deletar da sua lista: "));
        try:
            lista_de_compras.pop(deletar);
            for indice, item in enumerate(lista_de_compras):
                print(indice, item);  
        except:
            print("Não foi possivel apagar esse item :()") 

    elif (input_usuario.lower() == "l"):
        for indice, item in enumerate(lista_de_compras):
            print(indice, item);   

    else:
        print("Digite uma opção valida!")