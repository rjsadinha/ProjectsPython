'''
Problema:
   Um vendedor necessita de um algoritmo que calcule o preço total devido por
um cliente em compras. O algoritmo deve ler o nome do cliente, o código de um
produto e a quantidade comprada de cada item. Calcular o preço total por item.

    Quando o código digitado for 'fim' deve encerrar o programa e
mostrar o total a ser pago de todos itens digitados.

TABELA DE PRODUTOS E PREÇOS
Código do Produto - Preço unitário
            1001  - 5.32
            1324  - 6.45
            6548  - 2.37
            2987  - 5.32
            7623  - 6.45

EXEMPLO: Ao ser digitado 'fim' mostrar o resumo das compras:
----------------------------------------
Nome: Pedro
Produto - Qtd.  -      Preço
   1001  -  2   -      10.64
   2987  -  1   -       5.32
   6548  -  3   -       7.11
   Total:              23.07

'''

lista_produtos = ['1001', '1324', '6548', '2987', '7623']
lista_preços =   [ 5.32 ,  6.45 ,  2.37 ,  5.32 ,  6.45 ]
total = 0
lista_prods_compra = []
lista_qt_compra = []
lista_preco_itens = []

# ler o nome
nome_cliente = input("Digite Nome: ")

while True:
    # ler o código
    cod_compra = input("Digite o código: ")
    if cod_compra == 'fim':
        break
    if cod_compra in lista_produtos:
        # ler a quantidade
        qt_compra = int(input("Digite a quantidade: "))

        lista_prods_compra.append(cod_compra)
        lista_qt_compra.append(qt_compra)

        # calcular o preco do item
        for ind,ele in enumerate(lista_produtos):
            if cod_compra == ele:
                preco = lista_preços[ind]
                valor_item = qt_compra * preco
                lista_preco_itens.append(valor_item)

                # calcular o preço total
                total = total + valor_item
    else:
        input("Código digitado incorreto.")
print("\n==================================")
print(f"Nome: {nome_cliente}")
# ??? mostrar os produtos e quantidades dos itens
for ind in range(len(lista_prods_compra)):
    print(f"    {lista_prods_compra[ind].ljust(15,'.')} - {lista_qt_compra[ind]} - {lista_preco_itens[ind]}")
print(f"Total: {total}")