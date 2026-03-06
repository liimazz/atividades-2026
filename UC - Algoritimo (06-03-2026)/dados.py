# Quadardos de 1 a 10
quadrados = [x**2 for x in range (1,11)]
print ("Quadrados: ", quadrados)

# Números pares de 1 a 20
pares = [x for x in range (1,21) if x % 2 == 0]
print ("Pares: ", pares)

# Vogais de "PROGAMAÇÃO"
vogais = [letra for letra in "PROGAMAÇÃO" if letra in "AEIOU"]
print ("Vogais: ", vogais)