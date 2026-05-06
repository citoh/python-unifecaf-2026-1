# Desenvolva um CRUD de uma loja de roupas

import sqlite3
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) 
DB_PATH = SCRIPT_DIR + "/db_roupas.db"


def conectar():
    conexao = sqlite3.connect(DB_PATH)
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_tabela(conexao):
    cursor = conexao.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS roupas ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "descricao TEXT NOT NULL, "
        "marca TEXT NOT NULL)"
    )
    conexao.commit()


def inserir_roupa(conexao):
    print("\nRoupas cadastradas atualmente:")
    listar_roupas(conexao)

    nome = input("Descricao da roupa: ").strip()
    if not nome:
        print("Descricao invalida.")
        return

    marca = input("Marca: ").strip()
    if not marca:
        print("Marca invalida.")
        return
    try:
        conexao.execute(
            "INSERT INTO roupas (descricao, marca) VALUES (?, ?)",
            (nome, marca),
        )
        conexao.commit()
        print("Roupa cadastrada com sucesso.")
    except sqlite3.IntegrityError:
        print("Nao foi possivel cadastrar a roupa.")

def listar_roupas(conexao):
    roupas = conexao.execute(
        "SELECT id, descricao, marca FROM roupas ORDER BY id"
    ).fetchall()

    if not roupas:
        print("Nenhuma roupa cadastrada.")
        return
    
    for roupa in roupas:
        print(f"{roupa['id']}: {roupa['descricao']} - {roupa['marca']}")


def atualizar_roupa(conexao):
    print("\nRoupas cadastradas atualmente:")
    listar_roupas(conexao)

    id_texto = input("ID da roupa: ").strip()
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
        "UPDATE roupas SET descricao = ?, marca = ? WHERE id = ?",
        (novo_nome, nova_marca, int(id_texto)),
    )
    conexao.commit()

    if cursor.rowcount == 0:
        print("Roupa nao encontrada.")
    else:
        print("Dados da roupa atualizados com sucesso.")


def remover_roupa(conexao):
    print("\nRoupas cadastradas atualmente:")
    listar_roupas(conexao)

    id_texto = input("ID da roupa: ").strip()
    if not id_texto.isdigit():
        print("ID invalido.")
    return

    cursor = conexao.execute(
        "DELETE FROM roupas WHERE id = ?", 
        (int(id_texto),))
    conexao.commit() 

    if cursor.rowcount == 0:
        print("Roupa nao encontrada.")
    else:
        print("Roupa removida com sucesso.")


def buscar_roupa(conexao):
    termo = input("termo de busca:").strip()

    if not termo:
        print("termo invalido.")
    return

    termo_bucsa = "&" + termo + "&"
    roupas = conexao.execute(
        "SELECT id, descricao, marca FROM roupas "
        "WHERE descricao LIKE ? OR marca LIKE ? "
        "ORDER BY id",
        (termo_busca, termo_busca),
    ).fetchall()

    if not roupas:
        print("Nenhuma roupa encontrada.")
    else:
        print("\nRoupas encontradas:")
        for roupa in roupas:
            print(f"{roupa['id']}: {roupa['descricao']} - {roupa['marca']}")


def exibir_menu():
    print("\n=== MENU SQLITE ===")
    print("1 - Inserir roupa (lista antes)")
    print("2 - Listar roupas")
    print("3 - Atualizar roupa (descricao e marca)")
    print("4 - Remover roupa (lista antes)")
    print("5 - Buscar roupa por descricao ou marca")
    print("0 - Sair")



# INÍCIO =================================================


conexao = conectar()
criar_tabela(conexao)

while True:
    exibir_menu()
    opcao = input("Escolha uma opcao: ").strip()
    print()

    if opcao == "1":
        inserir_roupa(conexao)
    elif opcao == "2":
        listar_roupas(conexao)
    elif opcao == "3":
        atualizar_roupa(conexao)
    elif opcao == "4":
        remover_roupa(conexao)
    elif opcao == "5":
        buscar_roupa(conexao)
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opcao invalida.")
        
    print()
    input('Pressione qualquer tecla para continuar...')

conexao.close()
