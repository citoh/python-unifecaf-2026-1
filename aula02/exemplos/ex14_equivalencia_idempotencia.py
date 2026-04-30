# Lei da Idempotência

A = True

if A and A:
    print("Verdadeiro")
else:
    print("Falso")

# é equivalente à

if A:
    print("Verdadeiro")
else:
    print("Falso")