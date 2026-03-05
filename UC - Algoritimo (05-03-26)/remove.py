nomes = ["Ana,""Guilherme,""Cabral,""Daniela"]
print ("Nomes: ", nomes)

nomes.remove ("Ana")
print ("Lista atualizada: ", nomes)

#removido = nomes.pop()
removido = nomes.pop(1)
print (f"Removido: {removido}")
print ("Apos pop(): ", nomes)

#del - remover pelo indice
del nomes[0]
print ("Após del nomes [0] ", nomes)

# clear: esvaziar
nomes.clear()
print ("Lista atualizada: ", nomes)

