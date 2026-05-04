import ac3_estatisticas
import ac4_crud_completo
import exemplo_lendo_dados


def menu_principal():
    while True:
        print("\n========== PROJETO VENDAS ==========")
        print("1 - Exemplo: leituras basicas")
        print("2 - AC3: lista de exercicios de estatisticas")
        print("3 - AC4: lista de exercicios CRUD completo")
        print("0 - Sair")

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            exemplo_lendo_dados.menu()
        elif opcao == "2":
            ac3_estatisticas.listar_exercicios()
        elif opcao == "3":
            ac4_crud_completo.menu()
        elif opcao == "0":
            print("Encerrando o sistema.")
            break
        else:
            print("Opcao invalida. Tente novamente.")


if __name__ == "__main__":
    menu_principal()
