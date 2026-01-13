def adicionar_lancamento(lancamentos, valor_int, tipo):
    lancamentos.append({
        "valor": valor_int,
        "tipo": tipo
    })


def calcular_saldo(lancamentos):
    total = 0
    for lancamento in lancamentos:
        if lancamento["tipo"] == "entrada":
            total += lancamento["valor"]
        elif lancamento["tipo"] == "saida":
            total -= lancamento["valor"]
    return total
