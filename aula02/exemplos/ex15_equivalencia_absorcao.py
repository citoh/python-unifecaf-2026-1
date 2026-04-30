# Lei da Absorção

A = True
B = False

if A or (A and B):
    print("Verdadeiro")
else:
    print("Falso")

# é equivalente à

if A:
    print("Verdadeiro")
else:
    print("Falso")