import random

lista = [12, 5, 33, 18, 2, 27]
print("Lista original:", lista)

lista.sort()
print("Ordem crescente:", lista)

lista.sort(reverse=True)
print("Ordem decrescente:", lista)

random.shuffle(lista)
print("Lista embaralhada:", lista)