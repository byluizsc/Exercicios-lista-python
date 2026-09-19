produtos = []

for i in range(5):
    produto = input("Digite um produto: ")
    produtos.append(produto)

    print("Produtos cadastrados: ", produtos)
    print("Quantidade de produtos:", len(produtos))