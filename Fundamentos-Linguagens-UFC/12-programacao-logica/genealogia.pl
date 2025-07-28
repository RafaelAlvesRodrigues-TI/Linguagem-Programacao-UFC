% Base de conhecimento: genealogia

% Fatos
pai(joao, maria).
pai(joao, pedro).
mae(ana, maria).
mae(ana, pedro).

pai(pedro, carla).
mae(sofia, carla).

% Regras
irmao(X, Y) :- pai(P, X), pai(P, Y), mae(M, X), mae(M, Y), X \= Y.
avo(X, Y) :- pai(X, Z), pai(Z, Y).
avo(X, Y) :- pai(X, Z), mae(Z, Y).
avo(X, Y) :- mae(X, Z), pai(Z, Y).
avo(X, Y) :- mae(X, Z), mae(Z, Y).
