from enum import Enum

class TipoConta(Enum):
    CORRENTE = "Conta Corrente"
    POUPANCA = "Conta Poupança"

def cria_conta(numero, titular, saldo, tipo_conta, limite):
    conta = {
        "numero": numero,
        "titular": titular,
        "saldo": saldo,
        "tipo_conta": tipo_conta.value,
        "limite": limite
    }
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, tipo_conta, valor):
    if tipo_conta == TipoConta.CORRENTE and valor > conta["saldo"] + conta["limite"]:
        print("Saldo insuficiente e limite estourado.")
    elif tipo_conta == TipoConta.POUPANCA and valor > conta["saldo"]:
        print("Saldo insuficiente.")
    else:
        conta["saldo"] -= valor

def extrato(conta):
    print(f"Número da Conta: {conta['numero']}")
    print(f"Titular da Conta: {conta['titular']}")
    print(f"Tipo de Conta: {conta['tipo_conta']}")
    print(f"Saldo: R${conta['saldo']:.2f}")
    print(f"Limite: R${conta['limite']:.2f}")

# Função para criar uma nova conta com entrada do usuário
def criar_conta_com_input():
    numero = int(input("Número da Conta: "))
    titular = input("Titular da Conta: ")
    saldo = float(input("Saldo Inicial: "))
    tipo_conta = TipoConta[input("Tipo de Conta (CORRENTE ou POUPANCA): ")]
    limite = float(input("Limite de Crédito: "))
    return cria_conta(numero, titular, saldo, tipo_conta, limite)

# Exemplo de uso com interação do usuário
if __name__ == "__main__":
    contas = []

    # Exemplo de criação de conta com interação do usuário
    nova_conta = criar_conta_com_input()
    contas.append(nova_conta)
    print("Conta criada com sucesso!")

    while True:
        print("\nOpções:")
        print("1. Realizar Depósito")
        print("2. Realizar Saque")
        print("3. Exibir Extrato")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            numero_conta = int(input("Número da Conta para Depósito: "))
            valor_deposito = float(input("Valor do Depósito: "))
            for conta in contas:
                if conta["numero"] == numero_conta:
                    deposita(conta, valor_deposito)
                    print("Depósito realizado com sucesso!")

        elif escolha == "2":
            numero_conta = int(input("Número da Conta para Saque: "))
            tipo_conta_input = input("Tipo de Conta para Saque (1 para CORRENTE, 2 para POUPANCA): ")
            tipo_conta = TipoConta.CORRENTE if tipo_conta_input == "1" else TipoConta.POUPANCA
            valor_saque = float(input("Valor do Saque: "))
            for conta in contas:
                if conta["numero"] == numero_conta:
                    saca(conta, tipo_conta, valor_saque)
                    print("Saque realizado com sucesso!")

        elif escolha == "3":
            numero_conta = int(input("Número da Conta para Extrato: "))
            for conta in contas:
                if conta["numero"] == numero_conta:
                    extrato(conta)

        elif escolha == "4":
            break