numeros = []

for i in range(8):
    numero = int(input("Digite seu numero: "))
    numeros.append(numero)

positivos = 0
negativos = 0
zeros = 0

for numero in numeros:
    if numero >= 1:
        positivos += 1
    elif numero < 0:
        negativos += negativos + 1
    else:
        zeros = zeros + 1

print("Numeros: ", numeros)
print("Quantidade de Positivos: ", positivos)
print("Quantidade de negativos: ", negativos)
print("Zeros: ", zeros)