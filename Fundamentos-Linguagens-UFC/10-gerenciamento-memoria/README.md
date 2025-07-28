# Desafio 10 - Gerenciamento de Memória

## Objetivo

Comparar como ocorre o gerenciamento de memória em duas linguagens de programação distintas: **C** e **Python**.

---

## Comparativo

| Característica                    | C                           | Python                          |
|----------------------------------|-----------------------------|---------------------------------|
| Tipo de gerenciamento            | Manual                      | Automático                      |
| Alocação de memória              | `malloc`, `calloc`          | Feita automaticamente           |
| Liberação de memória             | `free`                      | Coleta de lixo (garbage collector) |
| Controle do programador          | Total                       | Limitado (gerenciado pela VM)   |
| Riscos comuns                    | Vazamento de memória, ponteiros inválidos | Poucos riscos, mas pode haver vazamento por ciclos de referência |
| Ferramentas disponíveis          | Valgrind, AddressSanitizer  | `gc` (mod), `tracemalloc`       |

---

## Exemplos

### C (Alocação manual)

```c
#include <stdlib.h>
#include <stdio.h>

int main() {
    int* v = (int*) malloc(sizeof(int) * 5);
    if (v == NULL) return 1;

    for (int i = 0; i < 5; i++) v[i] = i;
    
    free(v); // Importante liberar memória
    return 0;
}

//Python

v = [i for i in range(5)]
# O coletor de lixo vai liberar essa memória automaticamente

