saldo_inicial = 0

valor = int(input("Digite um valor: "))

while valor != 0 :

    saldo_inicial = saldo_inicial + valor

    if saldo_inicial < 0 :
        print("Atenção: saldo negativo")
    

    valor = int(input("Digite um valor: "))

print(saldo_inicial)