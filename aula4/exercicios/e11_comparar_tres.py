# Exercício 11
# Leia três números e mostre o maior.

a=float(input())
b=float(input())
c=float(input())
if a>=b and a>=c:
    print("Maior:",a)
elif b>=c:
    print("Maior:",b)
else:
    print("Maior:",c)
