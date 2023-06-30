def menu():
    menu = """
        DIGITE (Q) PARA SAIR\
        DIGITE (E) PARA EXTRATO\
        DIGITE (S) PARA SACAR\
        DIGITE (CC) PARA CRIAR CONTA\
        DIGITE (C) PARA CRIAR USUARIO\
        DIGITE (D) PARA DEPOSITAR
    """

    funcao = input(menu).upper()
    return funcao


def depositar(extrato, saldo, numero_deposito, lista_usuarios):
    cpf = input("Digite seu CPF: ")
    confirmar_usuario = verificar_usuario(cpf, lista_usuarios)
    if confirmar_usuario:
        valor = float(input("Digite o valor do deposito: "))

        saldo += valor
        numero_deposito += 1
        extrato[f"deposito_{numero_deposito}"] = f"R$ {valor:.2f}"
        return extrato, saldo, numero_deposito, lista_usuarios
    else:
        print("Usuário não localizado.\nCrie primeiramente um usuário na opção C")
        return extrato, saldo, numero_deposito, lista_usuarios


def sacar(extrato, saldo, numero_saque, lista_usuarios):
    cpf = input("Digite seu CPF: ")
    confirmar_usuario = verificar_usuario(cpf, lista_usuarios)
    if confirmar_usuario:
        valor = float(input("Digite o valor do saque: "))

        if numero_saque > 3:
            print("Você excedeu o numero de saque diário")
            return extrato, saldo, numero_saque, lista_usuarios
        elif valor > 500:
            print("Você excedeu o limite de valor por saque")
            return extrato, saldo, numero_saque, lista_usuarios

        elif valor < saldo:
            saldo -= valor
            numero_saque += 1
            extrato[f"saque_{numero_saque}"] = f"R$ {valor:.2f}"
            return extrato, saldo, numero_saque, lista_usuarios
        else:
            print("Valor acima do saldo na conta")
            return extrato, saldo, numero_saque, lista_usuarios

    else:
        print("Usuário não localizado.\nCrie primeiramente um usuário na opção C")
        return extrato, saldo, numero_saque, lista_usuarios


def emitir_extrato(extrato, saldo):
    print(f"EXTRATO: {extrato} | SALDO: {saldo}")


def criar_usuario(lista_usuarios):
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")
    validacao = validador_cpf(cpf, lista_usuarios)
    if validacao:
        endereco = input("Digite seu endereço: ")
        usuario = {"nome": nome, "cpf": cpf, "endereco": endereco}
        lista_usuarios.append(usuario)
        print("Usuário adicionado com sucesso")
        return lista_usuarios
    else:
        print("CPF não foi validado")
        return lista_usuarios


def validador_cpf(cpf, lista_usuarios):
    cpf = cpf.replace(".", "").replace("-", "")
    if cpf.isdigit() and len(cpf) == 11:
        ocorrencias = 0
        for cpf_usario in lista_usuarios:
            if cpf_usario["cpf"] == cpf:
                ocorrencias += 1
        if ocorrencias > 0:
            print("CPF DUPLICADO")
            return False
        else:
            print("CPF VÁLIDO")
            return True
    else:
        print("CPF INVÁLIDO")
        return False


def verificar_usuario(cpf, lista_usuarios):
    ocorrencias = 0
    for cpf_usario in lista_usuarios:
        if cpf_usario["cpf"] == cpf:
            ocorrencias += 1
    if ocorrencias > 0:
        return True
    else:
        return False


def main():
    lista_usuarios = []
    extrato = {}
    saldo = 0
    numero_deposito = 0
    numero_saque = 0
    while True:

        funcao = menu()

        if funcao == "D":
            extrato, saldo, numero_deposito, lista_usuarios = depositar(
                extrato, saldo, numero_deposito, lista_usuarios)

        elif funcao == "E":
            emitir_extrato(extrato, saldo)

        elif funcao == "C":
            lista_usuarios = criar_usuario(lista_usuarios)

        elif funcao == "S":
            extrato, saldo, numero_saque, lista_usuarios = sacar(
                extrato, saldo, numero_saque, lista_usuarios)

        elif funcao == "Q":
            print("Obrigado por utilizar nosso sistema")
            break


main()
