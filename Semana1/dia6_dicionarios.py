lancamentos = []

def calcular_saldo(lancamentos):
    total = 0
    for lancamento in lancamentos:
        if lancamento["tipo"] == "entrada":
            total += lancamento["valor"]
        elif lancamento["tipo"] == "saida":
            total -= lancamento["valor"]
    return total

def adicionar_lancamento(valor_int, tipo):
    lancamento = {
        "valor" : valor_int, 
        "tipo" : tipo
    }
    lancamentos.append(lancamento)



while  True:
    print("*********************")
    print("MENU")

    print("1 - Adicionar Entrada")
    print("2 - Adicionar Saida")
    print("3 - Mostrar Saldo")
    print("0 - Sair")
    

    opcao = input("Digite a opção desejada: ")
    print("*********************")
    opcao = opcao.strip().lower()

    if opcao == "1":
        valor = input("Digite um valor: ")
        valor = valor.strip().lower()
        
        if valor.isdigit():
            valor_int = int(valor)
            tipo = "entrada"
            adicionar_lancamento(valor_int, tipo)
            
    
        else:
            print("Valor Inválido")

    elif opcao == "2":
        valor = input("Digite um valor: ")
        valor = valor.strip().lower()
        
        if valor.isdigit():
            valor_int = int(valor)
            tipo = "saida"
            adicionar_lancamento(valor_int, tipo)

        else:
            print("Valor Inválido")

    elif opcao == "3":
        resultado = calcular_saldo(lancamentos)
        print("*********************")
        print(f"Soma total = {resultado}")

    elif opcao == "0":
        break

    else:
        print("Opção Inválida")
            

