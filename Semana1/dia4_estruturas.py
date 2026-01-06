#Criação de lista vazia
lista = []

#Função para add valores a lista 
def add_lista(valor):
    lista.append(valor)
    

#Somando valores da lista
def calcular_saldo(lista):
    total = 0
    for valor in lista:
        total += valor
    return total


while  True:
    print("*********************")
    print("MENU")

    print("1 - Adicionar Valor")
    print("2 - Mostrar Saldo")
    print("0 - Sair")
    

    opcao = input("Digite a opção desejada: ")
    print("*********************")
    opcao = opcao.strip().lower()


    if opcao == "1":
        valor = input("Digite um valor: ")
        valor = valor.strip().lower()
        
        if valor.isdigit():
            valor_int = int(valor)
            add_lista(valor_int)
        else:
            print("Valor Inválido")

    elif opcao == "2":
        resultado = calcular_saldo(lista)
        print("*********************")
        print(f"Soma total da lista = {resultado}")

    elif opcao == "0":
        break

    else:
        print("Opção Inválida")
            

