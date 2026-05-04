from banco_de_dados.conexao import conectar, fechar_conexao

def listar_vendedores():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome FROM vendedores")

        vendedores = cursor.fetchall()

        print("\n=== LISTA DE VENDEDORES ===")
        for vendedor in vendedores:
            print(f"ID: {vendedor[0]} | Nome: {vendedor[1]}")

        cursor.close()
        fechar_conexao(conexao)


def listar_produtos():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT id, descricao, preco FROM produtos")

        produtos = cursor.fetchall()

        print("\n=== LISTA DE PRODUTOS ===")
        for produto in produtos:
            print(f"ID: {produto[0]} | Descrição: {produto[1]} | Preço: R$ {produto[2]:.2f}")

        cursor.close()
        fechar_conexao(conexao)


def listar_vendas():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        sql = '''
            SELECT 
                vendas.id,
                vendedores.nome,
                vendas.data_e_hora,
                vendas.desconto,
                vendas.valor_final
            FROM vendas
            INNER JOIN vendedores
                ON vendas.id_vendedor = vendedores.id
            ORDER BY vendas.data_e_hora
        '''

        cursor.execute(sql)
        vendas = cursor.fetchall()

        print("\n=== LISTA DE VENDAS ===")
        for venda in vendas:
            print(
                f"Venda: {venda[0]} | "
                f"Vendedor: {venda[1]} | "
                f"Data: {venda[2]} | "
                f"Desconto: R$ {venda[3]:.2f} | "
                f"Valor Final: R$ {venda[4]:.2f}"
            )

        cursor.close()
        fechar_conexao(conexao)


def menu():
    while True:
        print("\n========== MENU ==========")
        print("1 - Listar vendedores")
        print("2 - Listar produtos")
        print("3 - Listar vendas")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_vendedores()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            listar_vendas()
        elif opcao == "0":
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()
