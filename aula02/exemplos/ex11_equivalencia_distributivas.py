# Leis Distributivas

A = True
B = False
C = True

if A and (B or C):
    print("Verdadeiro")
else:
    print("Falso")

# é equivalente à

if (A and B) or (A and C):
    print("Verdadeiro")
else:
    print("Falso")