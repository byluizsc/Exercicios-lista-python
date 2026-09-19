numeros = []

for i in range(7):
    numero = int(input("Digite seu numero: "))
    numeros.append(numero)

maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero

print("Numeros: ", numeros)
print("Maior numero: ", maior)