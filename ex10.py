notas = []
soma = 0
aprovados = 0
reprovados = 0

for i in range(10):
    nota = int(input("Digite sua nota: "))
    notas.append(nota)

for nota in notas:
    soma = soma + nota
    if nota >= 7:
        aprovados = aprovados + 1
    else: 
        reprovados = reprovados + 1

media = soma / len(notas)

print("Quantidade de notas: ", len(notas))
print("Media: ", media)
print("Aprovados: ", aprovados)
print("Reprovados: ", reprovados)