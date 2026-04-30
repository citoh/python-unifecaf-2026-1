import re

email = "usuario@email.com"
padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
if re.match(padrao, email):
    print("Email válido")
else:
    print("Email inválido")