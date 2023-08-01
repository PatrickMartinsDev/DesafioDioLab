import textwrap

def menu():
    menu = """\n
    ######## MENU ########

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tlistar contas
    [nu]\tNovo usuário
    [q]\tSair

    ######################

    ==>  """
    return input(textwrap.dedent(menu))

def depositar(saldo, deposito, extrato, /):
    if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R${deposito:.2f}\n"
            print(f"Depósito de R${deposito:.2f} realizado!")
    else:
        print("Operação falhou, o valor informado é inválido!")
    return saldo, extrato

def sacar(*, saldo, saque, extrato, limite, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = saque > saldo    
    excedeu_limite = saque > limite      
    excedeu_saque = numero_saques >= LIMITE_SAQUES
        
    if excedeu_saldo:
        print("Operação falhou. Você não tem saldo suficiente!")
    elif excedeu_limite:
        print("Operação falhou. O valor de saque excede o limite!")
    elif excedeu_saque:
        print("Operação falhou. Você excedeu a quantidade de saques diários!")
    elif saque > 0:
        saldo -= saque
        extrato += f"Saque R${saque:.2f}\n"
        numero_saques += 1
        print(f"Valor sacado: RS{saque:.2f}")
    else:
        print("Operação falhou. O valor informado é inválido!")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n############# EXTRATO #############")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R${saldo:.2f}")
    print("\n###################################")

def criar_usuario(cpf, usuarios):
    cpf = input("Informe o seu CPF (Somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Esse CPF já foi cadastrado!")
        return
    
    nome = input("Informe o seu nome completo: ")
    data_nascimento = input("Informe a sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o seu endereço (logradouro, nro - bairro -cidade/sigla estado: )")

    usuarios.append({"nome":nome, "data_nascimento": data_nascimento, "endereco": endereco})

    print("Usuário cadastrado com sucesso!!!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\ 
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = input(menu)
    # Depósito
        if opcao == "d":
            deposito = float(input("Digite o valor do depósito: "))
            
            saldo, extrato = depositar(saldo, deposito, extrato)
    # Saque
        elif opcao == "s":
            saque = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                saque=saque,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

    # Extrato             
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

    # Criar Usuário
        elif opcao =="nu":
            criar_usuario(usuarios)

    #Nova Conta
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
    # Sair da operação
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada")

    
main()