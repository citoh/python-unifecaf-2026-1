# Leis Associativas

A = True
B = True
C = False

if (A and B) and C:
    print("Verdadeiro")
else:
    print("Falso")

# é equivalente à

if A and (B and C):
    print("Verdadeiro")
else:
    print("Falso")