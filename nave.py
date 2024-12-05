class Nave:
    def __init__(self, nome, capacidade, local="Espaço"):
        self.nome = nome
        self.capacidade = capacidade
        self.local = local
        self.carga = 0

    def viajar(self, destino):
        self.local = destino.nome
        print(f"A nave {self.nome} chegou ao destino: {self.local}.")

    def carregar(self, quantidade):
        if self.carga + quantidade > self.capacidade:
            print("Carga excede a capacidade da nave!")
        else:
            self.carga += quantidade
            print(f"{quantidade} unidades de carga foram adicionadas à nave {self.nome}.")

    def descarregar(self):
        print(f"{self.carga} unidades de carga descarregadas da nave {self.nome}.")
        self.carga = 0


