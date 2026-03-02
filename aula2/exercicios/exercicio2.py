# aplicando a Lei de De Morgan,
# substituindo "and" por "or" e ajustando as negações

usuario_logado = False
tem_permissao = True

if usuario_logado and tem_permissao:
    print("Acesso permitido")
else:
    print("Acesso negado")

# seu código aqui abaixo:


if not (not usuario_logado or not tem_permissao):
    print("Acesso permitido")
else:
    print("Acesso negado")