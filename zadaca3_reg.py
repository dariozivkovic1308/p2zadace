import re

string = input('Unesite string: ')
pattern = r'^M.*[0-5].*B$'
match = re.search(pattern, string)

if match:
    print("Podudaranje pronađeno:", match.group())
else:
    print("Nema podudaranja.")
