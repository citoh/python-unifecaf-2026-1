# Exercício 4
# Leia duas notas e informe se o aluno foi aprovado (>=7) ou reprovado.

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
media = (n1+n2)/2
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
