import sys # sys é um biblioteca naitva do Python para processos junto ao SO

#Crianco uma variável de saída
output = "ALOCAÇÃO BASE EM BYTES ---------------------------------\n" # \n é quebra de linha

# types é do tipo dict e está armazenando valores dos tipos mais comuns de variáveis
types = {
    "int": 0,
    "float": 0.0,
    "bool": True,
    "str": "",
    "list": [],
    "tuple": (),
    "dict": {},
    "set": set(),
    "NoneType": None,
}

# lado que imprime o quanto cada valor dentro de types está ocupando da memória RAM
for name, value in types.items():
    output += f"{name:<8} ->  {sys.getsizeof(value)} bytes\n"

output += "\n"
output += "TESTE A SUA VARIÁVEL -----------------------------------\n"

# coloque o valor da sua variável
x = 1
output += f"Valor: {x}\n"
output += f"Tipo: {type(x).__name__}\n"
output += f"Bytes usados: {sys.getsizeof(x)}\n"
output += "\n"

# Imprime na tela o que temos na memória RAM (variável output)
print(output)


# EXTRA - Salvando em arquivo o que temos na memória RAM (variável output)
# with open("variaveis_dados.txt", "w", encoding="utf-8") as file:
#    file.write(output)