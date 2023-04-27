lista_cidades = []
lista_temperaturas = []


menu = """ 
    
    MENU
    1- Adicionar Cidade/Temperatura
    2- Excluir Cidade/Temperatura
    3- Alterar Temperatura
    4- Relatório
    5- Sair
    
    Escolha: """

while True:
    teclado = input(menu)

    if teclado == "1":
        # ler cidade
        cidade = input("Nova cidade: ").upper()
        # ler temperatura
        while True:
            try:
                temperatura = float(input("Temperatura em Celsius: ").replace(",",'.'))
                break
            except:
                input("Erro. ")


        # Verificar se cidade já existe
        if cidade not in lista_cidades:
            # adicionar cidade na lista de cidades
            lista_cidades.append(cidade)
            # adicionar temperatura na lista de temperaturas.
            lista_temperaturas.append(temperatura)
        else:
            input("Erro. Cidade já existe.")


    if teclado == "2":
        # ler cidade
        cidade = input("Cidade a ser excluida: ").upper()
        # verificar se existe
        for indice, cid in enumerate(lista_cidades):
            # Se existir
            if cidade == cid:
                #   excluir da lista de cidades
                lista_cidades.remove(cidade)
                #   excluir a temperatura na lista de temperaturas.
                lista_temperaturas.pop(indice)
                break



    if teclado == "3":
        # ler cidade
        cidade = input(" Cidade: ").upper()
        # verificar se cidade existe
        for ind, cid in enumerate(lista_cidades):
            # Se existir
            if cidade == cid:
                #   ler nova temperatura
                nova_temperatura = float(input("Nova Temperatura: ").replace(",","."))
                #   alterar o elemento.
                lista_temperaturas[ind] = nova_temperatura


    if teclado == "4":
        for ind in range(len(lista_cidades)):
            print(f"  {lista_cidades[ind]} - {lista_temperaturas[ind]}")
