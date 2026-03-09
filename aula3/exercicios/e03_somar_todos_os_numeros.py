# Enquanto o usuário não digitar 0 continue somando todos os números digitados
# n é um número informado pelo usuário
# dicas:
# - estrutura do while: while condição:
# - use input para ler o número n

soma = 0
n = int(input("Digite um número: "))

while n != 0:
    soma = soma + n
    n = int(input("Digite outro número (0 para parar): "))

print("Soma total:", soma)