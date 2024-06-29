def menu():
    menu = """
    BANCO - MENU

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Cadastrar usuário
    [5] Criar conta
    [6] Listar contas
    [0] Sair

    Digite uma opção => """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("=> Deposito realizado com sucesso")

    else:
        print("ERROR: Valor inválido para depósito")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("ERROR: Saldo insuficiente para saque")

    elif excedeu_limite:
        print("ERROR: Valor excede o limite de saque")

    elif excedeu_saques:
        print("ERROR: Número máximo de saques excedido")

    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato += f"Saque: R$ {valor:.2f}\n"
        print("=> Saque realizado com sucesso")

    else:
        print("ERROR: Valor inválido para saque")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n======= EXTRATO =======")
    print("\n=> Nenhuma movimentação realizada" if not extrato else extrato)
    print(f"=> Saldo: R$ {saldo:.2f}")
    print("========================")

def criar_usuario(usuarios):
    cpf = input("\nCPF (apenas números) => ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nERROR: CPF já cadastrado")
        return
    if len(cpf) != 11:
        print("\nERROR: CPF inválido")
        return

    nome = input("Nome completo => ")
    data_nascimento = input("Data de nascimento => ")
    endereco = input("Endereço (logradouro, num - bairro - cidade/UF)=> ")

    usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})
    print("\n=> Usuário cadastrado com sucesso")

def filtrar_usuario(cpf, usuarios):
    user_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return user_filtrados[0] if user_filtrados else None

def criar_conta(agencia, num_conta, usuarios):
    cpf = input("\nInforme o CPF => ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=> Conta criada com sucesso")
        return {"agencia": agencia, "num_conta": num_conta, "usuario": usuario}
    else:
        print("\nERROR: Usuário não encontrado")

def listar_contas(contas):
    for conta in contas:
        listar = f"""
            Agência: {conta['agencia']}
            Conta:  {conta['num_conta']}
            Titular:  {conta['usuario']['nome']}"""
        
        print(listar)

    if len(contas) == 0:
        print("\nERROR: Nenhuma conta cadastrada")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    usuarios = []
    contas =  []
    agencia = "0001"


    while True:
        opcao = menu()

        #depositar
        if opcao == "1":
            valor = float(input("\nValor do depósito => "))
            saldo, extrato = depositar(saldo, valor, extrato)

        #sacar
        elif opcao == "2":
            valor = float(input("\nValor do saque => "))
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = limite_saques)

        #extrato
        elif opcao == "3":
            exibir_extrato(saldo, extrato = extrato)

        #usuario
        elif opcao == "4":
            criar_usuario(usuarios)

        #conta
        elif opcao == "5":
            num_conta = len(contas) +1
            conta = criar_conta(agencia, num_conta, usuarios)

            if conta:
                contas.append(conta)

        #listar contas
        elif opcao == "6":
            listar_contas(contas)

        #sair
        elif opcao == "0":
            print("\n=> Operação finalizada!\n")
            break

        else:
            print("\nERROR: Opção inválida")

main()