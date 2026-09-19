numeros = []

for i in range(10):
   numero = int(input("Digite seu numero: "))
   numeros.append(numero)

pares = 0 
impares = 0

for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Quantidade de numeros pares: ", pares)
print("Quantidade de numeros impares", impares)