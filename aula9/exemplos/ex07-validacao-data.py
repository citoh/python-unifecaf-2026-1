from datetime import datetime

data = input("Digite sua data (DD/MM/AAAA): ")
try:
    datetime.strptime(data, "%d/%m/%Y")
    print("Data válida")
except:
    print("Data inválida")