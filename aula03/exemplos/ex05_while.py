import random

tentativas = 0
conexaoDB = False

while (not conexaoDB and tentativas < 5):
    conexaoDB = random.choice([True, False])
    tentativas += 1
    print(f"Tentativa {tentativas}: {'Sucesso' if conexaoDB else 'Falha'}")

if not conexaoDB:
    print('Não foi possível conectar após', tentativas, 'tentativas')
else:
    print('Conectado com sucesso!')