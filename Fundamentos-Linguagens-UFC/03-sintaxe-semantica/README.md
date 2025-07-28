# Desafio 03 - Descrições Sintáticas e Semânticas

## 🌐 Mini-gramática da linguagem fictícia "CalcLang"

<prog> ::= <stmt> ;
<stmt> ::= print <expr>
| let <id> = <expr>
<expr> ::= <expr> + <term>
| <expr> - <term>
| <term>
<term> ::= <term> * <factor>
| <term> / <factor>
| <factor>
<factor> ::= (<expr>)
| <num>
| <id>

### Exemplo de código em CalcLang:

let x = 5 + 3;
print x * 2;


### Análise léxica (tokens):
- `let` → palavra-chave
- `x` → identificador
- `=` → operador de atribuição
- `5`, `3` → números
- `+`, `*` → operadores
- `;` → delimitador de instrução
