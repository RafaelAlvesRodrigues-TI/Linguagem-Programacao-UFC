# Exemplo de programação funcional em Python

# Função de alta ordem: recebe outra função como argumento
def aplicar_operacao(lista, operacao):
    return [operacao(x) for x in lista]

# Função recursiva: calcular o n-ésimo número de Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Lista de números
valores = [1, 2, 3, 4, 5]

# Usando lambda para dobrar os valores
dobrados = aplicar_operacao(valores, lambda x: x * 2)

print("Valores dobrados:", dobrados)
print("Fibonacci(6):", fibonacci(6))
