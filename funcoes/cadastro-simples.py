def pode_entrar(idade):
    return idade >= 18

while True:
    nome = input("Nome (ou 'sair' para encerrar): ")

    if nome.lower() == "sair":
        print("Encerrando o programa...")
        break

    idade = int(input("Idade: "))

    if pode_entrar(idade):
        print(f"{nome}, você pode entrar.")
    else:
        print(f"{nome}, você não pode entrar.")
