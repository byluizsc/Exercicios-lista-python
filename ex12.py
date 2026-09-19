notas = []
soma = 0
aprovados = 0
reprovados = 0
alunos10 = 0
acima = 0

for i in range(10):
    nota = int(input("Digite sua nota: "))
    notas.append(nota)

for nota in notas:
    if nota >= 7:
        aprovados = aprovados + 1
    else:
        reprovados = reprovados + 1
    soma = soma + nota 
    media = soma / len(notas)
    if nota == 10:
        alunos10 = alunos10 + 1
    if nota > 7:
        acima = acima + 1

print("Quantidade de notas: ", notas)
print("Soma: ", soma)
print("Media: ", media)
print("Aprovados: ", aprovados)
print("Reprovados: ", reprovados)
print("Notas 10: ", alunos10)
print("Acima da media: ", acima)