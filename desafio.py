menu = """######## MENU ########

[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair

######################

==>  """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)
# Depósito
    if opcao == "d":
        deposito = float(input("Digite o valor do depósito: "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R${deposito:.2f}\n"
            print(f"Depósito de R${deposito} realizado!")
        else:
            print("Operação falhou, o valor informado é inválido!")
# Saque
    elif opcao == "s":
        saque = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = saque > saldo
        
        excedeu_limite = saque > limite
        
        excedeu_saque = numero_saques >= LIMITE_SAQUE
        
        if excedeu_saldo:
            print("Operação falhou. Você não tem saldo suficiente!")
        elif excedeu_limite:
            print("Operação falhou. O valor de saque excede o limite!")
        elif excedeu_saque:
            print("Operação falhou. Você excedeu a quantidade de saques diários!")
        elif saldo > 0:
            saldo -= saque
            extrato += f"Saque R${saque:.2f}\n"
            numero_saques += 1
            print(f"Valor sacado: RS{saque}")
        else:
            print("Operação falhou. O valor informado é inválido!")
# Extrato             
    elif opcao == "e":
        print("\n############# EXTRATO #############")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("\n###################################")
# Sair da operação
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")
