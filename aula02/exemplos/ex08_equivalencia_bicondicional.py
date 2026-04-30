# Lei da Bicondicional

acesso_premium = True
assinatura_ativa = False

if acesso_premium == assinatura_ativa:
    print("Regra OK (bicondicional verdadeira)")
else:
    print("Regra quebrada (bicondicional falsa)")
    
    
# é equivalente à 

if (acesso_premium and assinatura_ativa) or (not acesso_premium and not assinatura_ativa):
    print("Regra OK (bicondicional verdadeira)")
else:
    print("Regra quebrada (bicondicional falsa)")