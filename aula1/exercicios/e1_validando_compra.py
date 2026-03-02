# Crie 2 variáveis: 
#   -  compra_paga
#   -  produto_em_estoque
#
# Ao final imprima se o produto pode ou não ser vendido. 
# O produto apenas pode ser vendido se a compra já foi paga 
# e se houver produto no estoque

compra_paga = True
produto_em_estoque = True

if compra_paga and produto_em_estoque:
    print("Pode vender")
else:
    print("Não pode vender")