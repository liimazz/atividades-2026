senha_correta = "123456"
nome = input("Digite seu nome: ")

tentativas = 0

while tentativas < 3:
    senha = input("Digite sua senha: ")

    if senha == senha_correta:
        print(f"Olá, {nome}. Seja bem-vindo ao nosso banco!")
        break
    else:
        tentativas += 1

        if tentativas == 1:
            print("Senha incorreta! Você ainda tem 2 tentativas.")
        elif tentativas == 2:
            print("Senha incorreta! Você ainda tem 1 tentativa.")
        else:
            print("Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.")