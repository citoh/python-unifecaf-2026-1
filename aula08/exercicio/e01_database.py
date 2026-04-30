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
    return

def listar_roupas(conexao):
    return


def atualizar_roupa(conexao):
    return


def remover_roupa(conexao):
    return


def buscar_roupa(conexao):
    return


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
