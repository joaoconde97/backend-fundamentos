from caixa import calcular_saldo, adicionar_lancamento
from dados import salvar_lancamentos, carregar_lancamentos

lancamentos = carregar_lancamentos()

def ler_inteiro():
    while True:
        entrada = input("Digite um valor: ")
        try:
            valor = int(entrada)
            return valor
        except ValueError:
            print("Valor invalido. Digite um numero inteiro.")

while  True:
    print("*********************")
    print("MENU")

    print("1 - Adicionar Entrada")
    print("2 - Adicionar Saida")
    print("3 - Mostrar Saldo")
    print("0 - Sair")
    

    opcao = input("Digite a opção desejada: ")
    print("*********************")
    opcao = opcao.strip()

    if opcao == "1":
        tipo = "entrada"
        valor_int = ler_inteiro()
        adicionar_lancamento(lancamentos, valor_int, tipo)
        salvar_lancamentos(lancamentos)
    

    elif opcao == "2":
        tipo = "saida"
        valor_int = ler_inteiro()
        adicionar_lancamento(lancamentos, valor_int, tipo)
        salvar_lancamentos(lancamentos)


    elif opcao == "3":
        resultado = calcular_saldo(lancamentos)
        print("*********************")
        print(f"Soma total = {resultado}")

    elif opcao == "0":
        break

    else:
        print("Opção Inválida")