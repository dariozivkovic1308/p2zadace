import re

unos = input('Unesite e-mail adresu: ')
eduId = input('Unesite eduId adresu: ')

uzorak = '^[a-zA-Z]+\.[a-zA-Z]+\d*@fpmoz\.sum\.ba$'
eduIdUzorak = '^[a-zA-Z][a-zA-Z]+\d*@sum\.ba$'
match = re.search(uzorak, unos)
match2 = re.search(eduIdUzorak, eduId)

if match and match2:
  print(match.group())
  print(match2.group())
  print('Uspjesna prijava!')
else:
  print("Pattern not found")
