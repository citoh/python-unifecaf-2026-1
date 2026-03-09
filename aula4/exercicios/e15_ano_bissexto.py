# Exercício 15
# Leia um ano e informe se é bissexto.

ano=int(input())
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print("Bissexto")
else:
    print("Não é bissexto")
