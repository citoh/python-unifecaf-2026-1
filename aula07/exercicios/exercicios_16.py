palavra = "universidade"
i = 0
contador = 0

while i < len(palavra):
    if palavra[i] in "aeiou":
        contador += 1
    i += 1

print(contador)