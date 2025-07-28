# Exemplo de recursão simples: cálculo de fatorial com rastreamento da pilha de chamadas

def fatorial(n, nivel=0):
    print("  " * nivel + f"fatorial({n}) chamado")
    if n == 0 or n == 1:
        print("  " * nivel + f"Retorna 1")
        return 1
    else:
        resultado = n * fatorial(n - 1, nivel + 1)
        print("  " * nivel + f"Retorna {resultado}")
        return resultado

# Teste
print("Resultado final:", fatorial(4))
