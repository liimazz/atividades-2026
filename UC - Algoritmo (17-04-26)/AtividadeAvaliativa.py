#Questão 1

print ("Hello, World!")

#Questão 2

idade = int (input (" Qual é a tua idade? "))

if idade >= 16:
    print ("Pode votar!")
else:
    print ("Você ainda não pode votar.")

    #Questão 3

    total = 0

while True:
    valor = float (input ("Digite o valor do produto: "))
    
    if valor == 0:
        break
    
    total += valor

print ("Total da compra: ", total)

#Questão 4

def calcular (peso, altura):
    try:
        imc = peso / (altura ** 2)

        if imc < 18.5:
            print ("Magro")
        elif imc <= 24.9:
            print ("Normal")
        else:
            print ("Acima do peso")

    except:
        print ("Deu erro ae, confere os valores!")

#Questão 5

amigos = ["Daniel", "Zakin", "Natan", "Deivinho"]

quantidade = len (amigos)

if quantidade % 2 == 0:
    print ("Tem", quantidade, "amigos - número par")
else:
    print ("Tem", quantidade, "amigos - número ímpar")

    #Questão 6

    temperaturas = []

for i in range (7):
    temp = float ( input (f"Digite a temperatura do dia {i+1}: "))
    temperaturas.append (temp)

soma = 0

for t in temperaturas:
    soma += t

media = soma / 7

print ("A média da semana foi: ", media)

#Questão 7

vendas = [10, 15, 20, 7, 8, 13]

soma = 0

for v in vendas:
    if v % 2 == 0:
        soma += v

print ("Soma dos valores pares: ", soma)

#Questão 8

valor = float ( input("Digite o valor da compra: "))

if valor > 500:
    desconto = valor * 0.20
elif valor >= 200:
    desconto = valor * 0.10
else:
    desconto = 0

final = valor - desconto

print ("Valor final: ", final)

#Questão 9

notas = [6.5, 8.0, 7.5, 5.0, 9.2, 7.0]

contador = 0

for n in notas:
    if n > 7:
        contador += 1

print ("Quantidade de notas acima de 7: ", contador)

#Questão 10

frase = input ("Digite uma frase: ").lower()

vogais = "aeiou"
contador = 0

for letra in frase:
    if letra in vogais:
        contador += 1

print ("Quantidade de vogais: ", contador)

#Questão 11

idades = []

for i in range (5):
    idade = int ( input(f"Digite a idade {i+1}: "))
    idades.append (idade)

idades.sort()

print ("Idades em ordem crescente: ", idades)

#Questão 12

while True:
    print("\n1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "5":
        break

    try:
        n1 = float(input("Primeiro número: "))
        n2 = float(input("Segundo número: "))

        if opcao == "1":
            print("Resultado:", n1 + n2)
        elif opcao == "2":
            print("Resultado:", n1 - n2)
        elif opcao == "3":
            print("Resultado:", n1 * n2)
        elif opcao == "4":
            print("Resultado:", n1 / n2)
        else:
            print("Opção inválida")

    except:
        print("Erro nos dados")