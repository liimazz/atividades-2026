numero = int(input("Digite um número inteiro positivo: "))

if numero % 2 == 0:
    resultado = numero ** 2
    print("O número é par. Quadrado:", resultado)
else:
    resultado = numero ** 3
    print("O número é ímpar. Cubo:", resultado)