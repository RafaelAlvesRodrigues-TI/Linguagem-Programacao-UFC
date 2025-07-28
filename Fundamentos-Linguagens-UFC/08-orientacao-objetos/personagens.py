# Exemplo de Programação Orientada a Objetos com herança e polimorfismo

class Personagem:
    def __init__(self, nome):
        self.nome = nome

    def atacar(self):
        print(f"{self.nome} ataca com soco!")

class Mago(Personagem):
    def atacar(self):
        print(f"{self.nome} lança uma bola de fogo!")

class Guerreiro(Personagem):
    def atacar(self):
        print(f"{self.nome} ataca com espada!")

# Demonstração de polimorfismo
personagens = [
    Mago("Merlin"),
    Guerreiro("Arthur"),
    Personagem("Aldeão")
]

for p in personagens:
    p.atacar()
