class Colonia:
    def __init__(self, nome, recursos):
        self.nome = nome
        self.recursos = recursos

    def coletar_recursos(self, quantidade):
        self.recursos += quantidade
        print(f"A colônia {self.nome} coletou {quantidade} unidades de recursos.")



    def status(self):
        return f"Colônia {self.nome}: {self.recursos} unidades de recursos."


