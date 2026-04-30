numeros = [8, 3, 12, 5]
i = 0
menor = numeros[0]

while i < len(numeros):
    if numeros[i] < menor:
        menor = numeros[i]
    i += 1

print(menor)