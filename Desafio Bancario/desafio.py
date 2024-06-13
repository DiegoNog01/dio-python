menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        depositar_valor = int(input("Digite o valor do depósito: "))
        if depositar_valor > 0:
            saldo += depositar_valor
            extrato += f"Depósito: R$ {depositar_valor:.2f}\n"
        else:
            print("Valor inválido")
    
    elif opcao == "s":
        valor_sacar = int(input("Digite o valor de saque: "))
        if valor_sacar > saldo or valor_sacar >= 500:
            print("Valor inválido")
        else:
            if valor_sacar > 0 and numero_saques < LIMITE_SAQUES:
                saldo -= valor_sacar
                extrato = f"Saque: R$ {valor_sacar:.2f}\n"
                numero_saques += 1
            else:
                print()
                print("Operação inválida")

    elif opcao == "e":
        print("=========== EXTRATO ==========")
        if not extrato:
            print("Não foi realizado nenhuma operação")
        else:
            print(f"Saldo: {saldo:.2f}")
        print("=============================")
            
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida")
            

