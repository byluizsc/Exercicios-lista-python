notas = []
soma = 0

for i in range(5):
    nota = float(input("Digite sua nota:"))
    notas.append(nota)

for nota in notas:
    soma = soma + nota

quantidade = len(notas)
media = soma / len(notas)

print("Notas: ", notas)
print("Soma: ", soma)
print("Media: ", media)
print("Quantidade: ", quantidade)