# QUESTÃO 1 - Cálculo de Salário


salario_base = 3500.00
bonus = 800.00
desconto = 250.00

salario_bruto = salario_base + bonus
salario_liquido = salario_bruto - desconto

print("Salário bruto:", salario_bruto)
print("Salário líquido:", salario_liquido)

print("Tipo de salario_base:", type(salario_base))
print("Tipo de bonus:", type(bonus))
print("Tipo de desconto:", type(desconto))
print("Tipo de salario_bruto:", type(salario_bruto))
print("Tipo de salario_liquido:", type(salario_liquido))


# QUESTÃO 2 - Consumo de Combustível


distancia = 450
consumo_carro = 8
preco_litro = 5.50

litros_consumidos = distancia / consumo_carro
custo_total = litros_consumidos * preco_litro

print("\nDistância percorrida:", distancia, "km")
print("Consumo do carro:", consumo_carro, "km/l")
print("Litros consumidos:", litros_consumidos)
print("Custo total de combustível: R$", custo_total)


# QUESTÃO 3 - Conversão de Temperatura


fahrenheit = 32
celsius = (fahrenheit - 32) * 5 / 9

print("\nTemperatura em Fahrenheit:", fahrenheit)
print("Temperatura convertida para Celsius:", celsius)


# QUESTÃO 4 - Operadores de Atribuição


estoque = 100
print("\nEstoque inicial:", estoque)

estoque += 50
print("Após receber 50 unidades:", estoque)

estoque -= 30
print("Após vender 30 unidades:", estoque)

estoque -= 5
print("Após devolver 5 unidades:", estoque)


# QUESTÃO 5 - Cadastro de Aluno


nome = input("\nDigite o nome do aluno: ")
matricula = int(input("Digite a matrícula: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print("\n----- RELATÓRIO DO ALUNO -----")
print("Nome:", nome)
print("Matrícula:", matricula)
print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Média:", media)


# QUESTÃO 6 - Classificação de Idade


idade = int(input("\nDigite a idade do atleta: "))

if idade < 12:
    categoria = "Infantil"
elif idade < 18:
    categoria = "Juvenil"
elif idade < 60:
    categoria = "Adulto"
else:
    categoria = "Sênior"

print("Categoria:", categoria)
print("Bem-vindo à competição!")



# QUESTÃO 7 - Validação de Senha


senha = input("\nDigite uma senha: ")

tem_numero = any(char.isdigit() for char in senha)

if len(senha) >= 8 and tem_numero:
    print("Senha válida!")
else:
    print("Senha inválida!")


# QUESTÃO 8 - Desconto Progressivo


valor_compra = float(input("\nDigite o valor da compra: "))

if valor_compra < 100:
    desconto = 0
elif valor_compra < 500:
    desconto = valor_compra * 0.05
elif valor_compra < 1000:
    desconto = valor_compra * 0.10
else:
    desconto = valor_compra * 0.15

valor_final = valor_compra - desconto

print("Valor original: R$", valor_compra)
print("Desconto: R$", desconto)
print("Valor final: R$", valor_final)



# QUESTÃO 9 - Contagem Regressiva

contador = 10

while contador >= 0:
    print(contador)
    contador -= 1

print("Foguete lançado!")


# QUESTÃO 10 - Tabuada Customizável


numero = int(input("\nDigite um número para ver a tabuada: "))

for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)



# QUESTÃO 11 - Soma de Números Pares


soma = 0

for i in range(1, 101):
    if i % 2 == 0:
        soma += i

print("\nSoma dos números pares de 1 a 100:", soma)


# QUESTÃO 12 - Depósitos com Validação


total = 0
quantidade = 0

while True:
    deposito = float(input("\nDigite o valor do depósito (0 para sair): "))

    if deposito == 0:
        break

    total += deposito
    quantidade += 1

print("Total depositado: R$", total)
print("Quantidade de depósitos:", quantidade)