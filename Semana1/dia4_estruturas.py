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

valor = int(input("Digite um valor: "))

while valor != 0:

    add_lista(valor)
    valor = int(input("Digite um valor: "))


#Printando resultados
resultado = calcular_saldo(lista)
print(f"Lista = {lista}")
print(f"Soma total da lista = {resultado}")