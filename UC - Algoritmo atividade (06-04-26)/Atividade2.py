lista = []

i = 0
while i < 8:
    lista.append(int(input("manda um numero ai: ")))
    i += 1

print("lista:", lista)

ja_foi = []

for a in lista:
    if a not in ja_foi:
        c = lista.count(a)
        if c > 1:
            print("o numero", a, "apareceu", c, "vezes kkk")
        ja_foi.append(a)