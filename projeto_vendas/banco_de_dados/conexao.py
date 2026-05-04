import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='projeto_vendas_eletronicos_unifecaf'
        )

        if conexao.is_connected():
            print("Conectado ao MySQL com sucesso!")
            return conexao

    except Error as e:
        print(f"Erro ao conectar: {e}")
        return None


def fechar_conexao(conexao):
    if conexao and conexao.is_connected():
        conexao.close()
        print("Conexão encerrada.")