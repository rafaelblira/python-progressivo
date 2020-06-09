import re

while True:
 texto = input("Numero no formato 'xxxx-yyyy': " )
 minhaRegex = re.findall(r'\d{4}-\d{4}', texto)

 print(minhaRegex)