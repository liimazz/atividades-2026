# 1.
def rank_jogador(pontos, derrotas):
    pontos = pontos - (derrotas * 10)

    if pontos < 0:
        return "Banido"
    if pontos < 100:
        return "Bronze"
    if pontos < 300:
        return "Prata"
    if pontos < 600:
        return "Ouro"
    return "Diamante"


# 2.
def saldo_final(saldo, saque):
    if saque > saldo:
        return "Saldo insuficiente"
    
    if saque > 1000:
        saque = saque + (saque * 0.02)
    
    return saldo - saque


# 3.
def tipo_magia(fogo, agua):
    if fogo == True and agua == True:
        return "Vapor"
    if fogo == True:
        return "Fogo"
    if agua == True:
        return "Água"
    return "Sem magia"


# 4.
def pontuacao_total(pontos, tempo):
    if tempo < 30:
        pontos += 50
    if tempo > 100:
        pontos -= 20

    if pontos > 200:
        return "Recorde"
    
    return pontos


# 5.
def verificar_acesso(usuario, senha, tentativas):
    if tentativas >= 3:
        return "Bloqueado"
    
    if usuario == "admin" and senha == "1234":
        return "Acesso total"
    
    if usuario == "admin" and senha != "1234":
        return "Senha incorreta"
    
    return "Usuário inválido"


# 6.
def lancar_foguete(combustivel, clima, sistema_ok):
    if combustivel < 100:
        return "Combustível insuficiente"
    
    if clima != "bom":
        return "Clima desfavorável"
    
    if sistema_ok == False:
        return "Falha no sistema"
    
    return "Lançamento autorizado"