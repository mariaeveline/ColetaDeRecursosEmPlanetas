from colonia import Colonia

class Planeta(Colonia):
    def __init__(self, nome, recursos, clima):
        super().__init__(nome, recursos)
        self.clima = clima

    def coletar_recursos(self, quantidade):
        if self.clima == "hostil":
            print(f"Clima hostil no planeta {self.nome}! Coleta reduzida pela metade.")
            quantidade //= 2
        super().coletar_recursos(quantidade)

    def status(self):
        return super().status() + f" Clima: {self.clima}."