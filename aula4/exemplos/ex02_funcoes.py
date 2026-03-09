# Função de Soma
def add(a, b):
    return a + b

# Função de Subtração
def subtract(a, b):
    return a - b

# Função de Multiplicação
def multiply(a, b):
    return a * b 


# Função de Divisão
def divide(a, b):
    if b == 0:
        return None
    return a / b

# Função com chamadas para outras funções
def printOperations(a, b):
    print(f"{a} + {b} =", add(a, b))
    print(f"{a} - {b} =", subtract(a, b))
    print(f"{a} * {b} =", multiply(a, b))
    print(f"{a} / {b} =", divide(a, b))

#Exemplo de como executar uma função
x = 10
y = 2
printOperations(x, y)