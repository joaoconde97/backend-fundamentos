#Função de Soma
# def soma(first_number, second_number):
#     resultado = first_number + second_number
#     return resultado

# resultado = soma(12,15)
# print(resultado)
#############################

#Função de Validação
# def validacao(number):
#     if number >= 0:
#         return True
#     elif number < 0:
#         return False
    
# resultado = validacao(-23)
# print(resultado)
#############################

#Função de Media
# def media(n1, n2, n3):
#     soma = n1 + n2 + n3
#     resultado = soma / 3
#     return resultado

# resultado = media(10, 8, 5)
# print(f"{resultado:.1f}")
#############################

#DESAFIO FINAL 

valor = int(input("Digite o valor: "))
saldo = 0

def atualizar_saldo(saldo,valor):
    novo_saldo = saldo + valor
    return novo_saldo

def alerta_negativo(saldo):
    if saldo < 0:
        print("Atenção, saldo negativo!")

while valor != 0 :
    saldo = atualizar_saldo(saldo, valor)
    alerta_negativo(saldo)
    valor = int(input("Digite o valor: "))

print(saldo)