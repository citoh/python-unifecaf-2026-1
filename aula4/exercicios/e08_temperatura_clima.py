# Exercício 8
# Leia uma temperatura e classifique: frio (<15), ameno (15-25), quente (>25).

t = float(input("Temperatura: "))
if t < 15:
    print("Frio")
elif t <= 25:
    print("Ameno")
else:
    print("Quente")
