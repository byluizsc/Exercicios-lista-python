numeros = []
soma = 0

for i in range(5):
    numero = float(input("Digite suas notas: "))
    numeros.append(numero)

for numero in numeros:
    soma = soma + numero

print("Numeros: ", numeros)
print("Soma: ", soma)
