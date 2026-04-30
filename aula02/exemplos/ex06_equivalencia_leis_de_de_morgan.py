# Leis de De Morgan

usuario_logado = False
usuario_pago = False

if not (usuario_logado and usuario_pago):
    print("Acesso negado")

# é equivalente a

if not usuario_logado or not usuario_pago:
    print("Acesso negado")