# Reescreva o algoritmo abaixo usando apenas operadores lógicos (and, or, not)
# sem utilizar comparação direta (==)

acesso_premium = True
assinatura_ativa = False

if acesso_premium == assinatura_ativa:
    print("Acesso correto")
else:
    print("Inconsistência detectada")

# seu código aqui abaixo:

if (acesso_premium and assinatura_ativa) or (not acesso_premium and not assinatura_ativa):
    print("Acesso correto")
else:
    print("Inconsistência detectada")