menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3
numero_depositos = 0

while True:

    opcao = input(menu)

    if opcao == "d":
        num_dep = float(input("Insira um valor a ser depositado: "))
        if num_dep < 0:
            print("Insira um valor valido!")
        else:
            saldo += num_dep
            numero_depositos += 1
            extrato += f"Deposito R${num_dep:.2f}\n"

    elif opcao == "s":
        LIMITE_SAQUES -= 1
        if LIMITE_SAQUES == 0:
            print("Numeros maximo de saques diários atingidos")
        else:
            num_saq = float(input("Insira um valor para ser retirado: "))
            if num_saq > limite:
                    print("Voce ultrapassou o limite!")
            else:
                if num_saq > saldo:
                    print("Saldo Insuficiente!")
                else:
                    saldo -= num_saq
                    numero_saque += 1
                    extrato += f"Saque R${num_saq:.2f}\n"
                    print("Sacado!")

    elif opcao == "e":
        if extrato:
            print(extrato)
        else:
            print("Não houve nenhuma transação!")
        print(f"Saldo Atual é : R${saldo}")
    
    elif opcao == "q":
        break