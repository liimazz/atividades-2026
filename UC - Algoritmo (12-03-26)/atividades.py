#1 atividade
numero = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))


def numeros (numero, numero2):
    S = numero + numero2
    M = numero * numero2
    return S, M

R = numeros (numero, numero2)
print (f"A soma e o produto é igual a {R}")


# 2 atividade
def processar_dados(vh, hd, dm=22):
    return (vh * hd * dm) + (1100 if hd > 8 else 0)

v = float(input("Infome o valor: "))
h = int(input("Informe o tempo: "))

print(f"Total mensal: {processar_dados(v, h):.2f}")