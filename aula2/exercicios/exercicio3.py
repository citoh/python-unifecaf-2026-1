# Reescreva o algoritmo abaixo sunstituindo o or por "and", 
# mas retornando os mesmos valores finais

usuario_admin = False
pode_excluir = True

if usuario_admin or pode_excluir:
    print("Usuário removido")
else:
    print("Não tem permissão para remover o usuário")

# seu código aqui abaixo:

if not (not usuario_admin and not pode_excluir):
    print("Usuário removido")
else:
    print("Não tem permissão para remover o usuário")
