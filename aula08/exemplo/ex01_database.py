import sqlite3
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = SCRIPT_DIR + "/db_carros.db"


def conectar():
    conexao = sqlite3.connect(DB_PATH)
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_tabela(conexao):
    # Tabela de automoveis
    cursor = conexao.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS carros ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "nome TEXT NOT NULL, "
        "marca TEXT NOT NULL)"
    )
    conexao.commit()


def inserir_carro(conexao):
    print("\nCarros cadastrados atualmente:")
    listar_carros(conexao)

    nome = input("Nome do carro: ").strip()
    if not nome:
        print("Nome invalido.")
        return

    marca = input("Marca: ").strip()
    if not marca:
        print("Marca invalida.")
        return

    try:
        conexao.execute(
            "INSERT INTO carros (nome, marca) VALUES (?, ?)",
            (nome, marca),
        )
        conexao.commit()
        print("Carro cadastrado com sucesso.")
    except sqlite3.IntegrityError:
        print("Nao foi possivel cadastrar o carro.")


def listar_carros(conexao):
    carros = conexao.execute(
        "SELECT id, nome, marca FROM carros ORDER BY id"
    ).fetchall()

    if not carros:
        print("Nenhum carro cadastrado.")
        return

    for carro in carros:
        print(f"[{carro['id']}] {carro['nome']} - {carro['marca']}")


def atualizar_carro(conexao):
    print("\nCarros cadastrados atualmente:")
    listar_carros(conexao)

    id_texto = input("ID do carro: ").strip()
    if not id_texto.isdigit():
        print("ID invalido.")
        return

    novo_nome = input("Novo nome: ").strip()
    if not novo_nome:
        print("Nome invalido.")
        return

    nova_marca = input("Nova marca: ").strip()
    if not nova_marca:
        print("Marca invalida.")
        return

    cursor = conexao.execute(
        "UPDATE carros SET nome = ?, marca = ? WHERE id = ?",
        (novo_nome, nova_marca, int(id_texto)),
    )
    conexao.commit()

    if cursor.rowcount == 0:
        print("Carro nao encontrado.")
    else:
        print("Dados do carro atualizados com sucesso.")


def remover_carro(conexao):
    print("\nCarros cadastrados atualmente:")
    listar_carros(conexao)

    id_texto = input("ID do carro para remover: ").strip()
    if not id_texto.isdigit():
        print("ID invalido.")
        return

    cursor = conexao.execute(
        "DELETE FROM carros WHERE id = ?",
        (int(id_texto),),
    )
    conexao.commit()

    if cursor.rowcount == 0:
        print("Carro nao encontrado.")
    else:
        print("Carro removido com sucesso.")


def buscar_carro(conexao):
    termo = input("Digite o termo de busca: ").strip()

    if not termo:
        print("Termo invalido.")
        return

    termo_busca = "%" + termo + "%"
    carros = conexao.execute(
        "SELECT id, nome, marca FROM carros "
        "WHERE CAST(id AS TEXT) LIKE ? OR nome LIKE ? OR marca LIKE ? "
        "ORDER BY id",
        (termo_busca, termo_busca, termo_busca),
    ).fetchall()

    if not carros:
        print("Nenhum carro encontrado.")
        return

    print("\nResultado da busca:")
    for carro in carros:
        print(f"[{carro['id']}] {carro['nome']} - {carro['marca']}")


def exibir_menu():
    print("\n=== MENU SQLITE ===")
    print("1 - Inserir carro (lista antes)")
    print("2 - Listar carros")
    print("3 - Atualizar carro (nome e marca)")
    print("4 - Remover carro (lista antes)")
    print("5 - Buscar carro por nome, marca ou id")
    print("0 - Sair")



# INÍCIO =================================================


conexao = conectar()
criar_tabela(conexao)

while True:
    exibir_menu()
    opcao = input("Escolha uma opcao: ").strip()
    print()

    if opcao == "1":
        inserir_carro(conexao)
    elif opcao == "2":
        listar_carros(conexao)
    elif opcao == "3":
        atualizar_carro(conexao)
    elif opcao == "4":
        remover_carro(conexao)
    elif opcao == "5":
        buscar_carro(conexao)
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opcao invalida.")
        
    print()
    input('Pressione qualquer tecla para continuar...')

conexao.close()
