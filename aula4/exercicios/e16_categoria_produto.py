# Exercício 16
# Leia o preço e classifique: barato(<50), médio(<100), caro.

p=float(input())
if p<50:
    print("Barato")
elif p<100:
    print("Médio")
else:
    print("Caro")
