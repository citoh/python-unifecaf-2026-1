# Avaliação Continuada 4 - 1 ponto
# PROJETO DE VENDAS - parte 2
# Exercicios de CRUD completo (Produtos, Vendedores e Vendas)
# Entrega - dia 23/05/2026


# PRODUTOS

def criar_produto():
    # Exercicio 1: cadastrar um novo produto na tabela produtos (descricao, preco).
    return


def listar_produtos():
    # Exercicio 2: listar todos os produtos cadastrados com id, descricao e preco.
    return


def atualizar_produto():
    # Exercicio 3: atualizar descricao e/ou preco de um produto existente por id.
    return


def excluir_produto():
    # Exercicio 4: excluir um produto por id, tratando dependencias em vendas_produtos.
    return


# VENDEDORES

def criar_vendedor():
    # Exercicio 5: cadastrar um novo vendedor na tabela vendedores.
    return


def listar_vendedores():
    # Exercicio 6: listar todos os vendedores cadastrados.
    return


def atualizar_vendedor():
    # Exercicio 7: atualizar o nome de um vendedor existente por id.
    return


def excluir_vendedor():
    # Exercicio 8: excluir vendedor por id, validando se possui vendas vinculadas.
    return


# VENDAS

def criar_venda_com_itens():
    # Exercicio 9: criar uma venda e inserir itens na tabela vendas_produtos com quantidade e valores.
    return


def listar_vendas_completas():
    # Exercicio 10: listar vendas com vendedor e itens (produto, quantidade, valor_unitario, valor_total).
    return


def atualizar_venda_e_itens():
    # Exercicio 11: atualizar dados da venda (desconto/valor_final) e seus itens.
    return


def excluir_venda():
    # Exercicio 12: excluir uma venda por id removendo primeiro os itens de vendas_produtos.
    return


def menu():
    opcoes = {
        "1": ("Criar produto", criar_produto),
        "2": ("Listar produtos", listar_produtos),
        "3": ("Atualizar produto", atualizar_produto),
        "4": ("Excluir produto", excluir_produto),
        "5": ("Criar vendedor", criar_vendedor),
        "6": ("Listar vendedores", listar_vendedores),
        "7": ("Atualizar vendedor", atualizar_vendedor),
        "8": ("Excluir vendedor", excluir_vendedor),
        "9": ("Criar venda com itens", criar_venda_com_itens),
        "10": ("Listar vendas completas", listar_vendas_completas),
        "11": ("Atualizar venda e itens", atualizar_venda_e_itens),
        "12": ("Excluir venda", excluir_venda),
    }

    while True:
        print("\n=== MENU AC4 - CRUD COMPLETO ===")
        for codigo, (descricao, _) in opcoes.items():
            print(f"{codigo} - {descricao}")
        print("0 - Voltar")

        escolha = input("Escolha uma opcao: ").strip()

        if escolha == "0":
            print("Voltando ao menu principal.")
            break

        if escolha in opcoes:
            descricao, funcao = opcoes[escolha]
            print(f"\nSelecionado: {descricao}")
            funcao()
            print("Exercicio em estrutura base (return vazio).")
        else:
            print("Opcao invalida. Tente novamente.")
