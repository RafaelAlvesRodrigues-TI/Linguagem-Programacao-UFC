# Desafio 12 - Programação Lógica

## Objetivo

Modelar um problema lógico usando conceitos de programação declarativa, como os encontrados em Prolog.

## Exemplo: Árvore Genealógica

### Fatos

Indicamos relações básicas como `pai/2` e `mae/2`.

### Regras

Definimos relações compostas, como:

- `irmao(X, Y)`: dois indivíduos que têm os mesmos pais.
- `avo(X, Y)`: X é avô ou avó de Y.

## Código

O código está no arquivo `genealogia.pl`.

### Como testar

Você pode usar o [SWI-Prolog](https://www.swi-prolog.org/) para executar:

```prolog
?- consult('genealogia.pl').
?- irmao(maria, pedro).
?- avo(joao, carla).
