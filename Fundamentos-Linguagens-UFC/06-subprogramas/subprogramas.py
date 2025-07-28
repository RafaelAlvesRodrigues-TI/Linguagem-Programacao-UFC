# Demonstração de passagem por valor e por referência em Python

def modifica_valor(x):
    x = x + 10
    print("Dentro da função (valor):", x)

def modifica_lista(lista):
    lista.append(100)
    print("Dentro da função (referência):", lista)

# Passagem por valor (imutável)
a = 5
print("Antes da função (valor):", a)
modifica_valor(a)
print("Depois da função (valor):", a)

print("---")

# Passagem por referência (mutável)
b = [1, 2, 3]
print("Antes da função (referência):", b)
modifica_lista(b)
print("Depois da função (referência):", b)
