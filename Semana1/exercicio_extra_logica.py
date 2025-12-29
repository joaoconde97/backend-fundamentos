saldo = 0

valor = int(input("Digite um valor: "))

while valor != 0 :

    saldo = saldo + valor

    if saldo < 0 :
        print("Atenção: saldo negativo")
    

    valor = int(input("Digite um valor: "))

print(saldo)