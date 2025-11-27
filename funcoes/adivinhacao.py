def jogo_adivinha():
    segredo = 7
    tentativas = 0
    
    while True:
        chute = int(input("Adivinhe o número (0–10): "))
        tentativas += 1

        if chute == segredo:
            print("Acertou!")
            break
        elif chute < segredo:
            print("Muito baixo!")
        else:
            print("Muito alto!")

    print(f"Você acertou em {tentativas} tentativas!")
