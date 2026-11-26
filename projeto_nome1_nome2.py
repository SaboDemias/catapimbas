def exibir_menu():
    """Exibe as opções do sistema para o usuário."""
    print("\n" + "=" * 40)
    print("          SISTEMA DE PRODUTOS")
    print("=" * 40)
    print("1. Cadastrar novo produto")
    print("2. Listar todos os produtos")
    print("3. Buscar produto (por ID ou Nome)")
    print("4. Remover produto")
    print("5. Sair")
    print("6. destrua o seu computador")
    print("=" * 40)


def cadastrar(produtos):
    """Cadastra um novo produto na lista usando append()."""
    print("\n--- CADASTRAR PRODUTO ---")
    try:
        id_prod = int(input("Digite o identificador (número inteiro): "))
    except ValueError:
        print("Erro: O identificador deve ser um número inteiro.")
        return

    for item in produtos:
        if item["id"] == id_prod:
            print("Erro: Já existe um produto com esse identificador")
            return

    nome = input("Digite o nome do produto: ").strip()
    if not nome:
        print("Erro O nome não pode ficar em branco")
        return

    try:
        preco = float(input("Digite o preço (ex: 5.50): ").replace(",", "."))
        if preco < 0:
            print("Erro: O preço não pode ser negativo")
            return
    except ValueError:
        print("Erro: Digite um valor numérico válido para o preço.")
        return

    novo_produto = {"id": id_prod, "nome": nome, "preco": preco}
    produtos.append(novo_produto)
    print("Produto cadastrado com sucesso!")


def listar(produtos):
    """Exibe todos os produtos de forma formatada"""
    print("\n--- LISTA DE PRODUTOS ---")
    if not produtos:
        print("Nenhum produto cadastrado no momento.")
        return

    print(f"{'ID':<6} | {'NOME':<18} | {'PREÇO'}")
    print("-" * 40)
    for item in produtos:
        print(f"{item['id']:<6} | {item['nome']:<18} | R$ {item['preco']:.2f}")


def busca_sequencial(produtos, termo):
    """Busca sequencialmente por ID ou Nome."""
    comparacoes = 0
    for indice, item in enumerate(produtos):
        comparacoes += 1
        if str(item["id"]) == termo or item["nome"].lower() == termo.lower():
            return indice, comparacoes

    return -1, comparacoes


def buscar(produtos):
    """Solicita o termo de busca e informa o resultado."""
    print("\n--- BUSCAR PRODUTO ---")
    if not produtos:
        print("A lista está vazia >:(")
        return

    termo = input("Digite o ID ou o Nome para buscar: ").strip()
    indice, comparacoes = busca_sequencial(produtos, termo)

    if indice != -1:
        encontrado = produtos[indice]
        print(f"\nProduto encontrado na posição {indice}:")
        print(
            f"ID: {encontrado['id']} | Nome: {encontrado['nome']} | Preço: R$ {encontrado['preco']:.2f}"
        )
    else:
        print("\nProduto não encontrado.")

    print(f"Total de comparações realizadas: {comparacoes}")


def remover(produtos):
    """Busca um produto e o remove da lista usando pop()."""
    print("\n--- REMOVER PRODUTO ---")
    if not produtos:
        print("A lista está vazia")
        return

    termo = input("Digite o ID ou o Nome do produto a remover: ").strip()
    indice, _ = busca_sequencial(produtos, termo)

    if indice != -1:
        removido = produtos.pop(indice)
        print(
            f"Produto '{removido['nome']}' (ID: {removido['id']}) removido com sucesso!"
        )
    else:
        print("Produto não encontrado :(")


def main():
    # Lista inicial :p
    produtos = [
        {"id": 1, "nome": "manga", "preco": 5.0},
        {"id": 2, "nome": "banana", "preco": 2.0},
        {"id": 3, "nome": "abacaxi", "preco": 7.0},
    ]

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == "1":
            cadastrar(produtos)
        elif opcao == "2":
            listar(produtos)
        elif opcao == "3":
            buscar(produtos)
        elif opcao == "4":
            remover(produtos)
        elif opcao == "5":
            print("\nEncerrando o programa...")
            break
        else:
            print("\nOpção inválida sla")


if __name__ == "__main__":
    main()