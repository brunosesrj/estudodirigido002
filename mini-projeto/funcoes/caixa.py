def sistema_caixa():
   
    nome = input("Nome do cliente: ")
    saldo = float(input("Saldo disponível: R$ "))


    print("\n--- Produtos disponíveis ---")
    print("1 - Camiseta  (R$ 50)")
    print("2 - Boné      (R$ 30)")
    print("3 - Jaqueta   (R$ 120)")

   
    escolha = int(input("\nEscolha um produto (1, 2 ou 3): "))
    quantidade = int(input("Quantidade: "))

   
    if escolha == 1:
        preco = 50
        produto = "Camiseta"
    elif escolha == 2:
        preco = 30
        produto = "Boné"
    elif escolha == 3:
        preco = 120
        produto = "Jaqueta"
    else:
        print("Produto inválido.")
        return

    total = preco * quantidade
    print(f"\nVocê escolheu {quantidade}x {produto}. Total: R$ {total}")

    # 5. Checar se pode pagar
    if total <= saldo:
        # 6. Debitar do saldo
        saldo -= total
        print("\nPagamento aprovado!")
    else:
        print("\nSaldo insuficiente!")
        return

    # 7. Mostrar saldo final
    print(f"Saldo final de {nome}: R$ {saldo}")