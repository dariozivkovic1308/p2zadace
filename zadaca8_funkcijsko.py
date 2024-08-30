def poz(ime):
    return f"Pozdrav {ime}!"

dobrodosao = lambda ime: f"Dobrodošao {ime}!"

def nova(xPozdrav, ime):
    return xPozdrav(ime)


ime = input("Unesite ime: ")
print(nova(poz,ime))
print(nova(dobrodosao, ime))
