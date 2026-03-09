# Exercício 7
# Leia o valor de uma compra. Se for maior que 100, aplique 10% de desconto.

valor = float(input("Valor da compra: "))
if valor > 100:
    valor = valor * 0.9
print("Total:", valor)
