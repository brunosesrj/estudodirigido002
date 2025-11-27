def verifica_pagamento(forma, valor):
    forma = forma.lower()

    if forma == "cartao" and valor > 20:
        return "Aceito!"
    elif forma == "pix":
        return "Aceito!"
    elif forma == "dinheiro" and valor == 10:
        return "Aceito!"
    else:
        return "Não aceito."


# Loop com 3 pedidos
for i in range(3):
    print(f"\nPedido {i + 1}:")
    forma = input("Forma de pagamento: ").lower()
    valor = float(input("Valor: "))

    resultado = verifica_pagamento(forma, valor)
    print(resultado)
