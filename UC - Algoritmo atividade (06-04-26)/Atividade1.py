import random

n = random.randint(1,100)
t = 0

print("to pensando num numero ai de 1 a 100... tenta adivinhar kkk")

while True:
    x = int(input("chuta: "))
    t = t + 1

    if x != n:
        if x < n:
            print("maior ai mano")
        else:
            print("menor né")
    else:
        print("acertou finalmente mds")
        break

print("vc tentou tipo", t, "vezes 👍")