from planeta import Planeta
from nave import Nave

def main():
    # Criando planetas
    planeta1 = Planeta("Marte", 100, "ameno")
    planeta2 = Planeta("Vênus", 50, "hostil")

    # Criando nave
    nave = Nave("Exploradora-1", 200)

    # Ações
    print(planeta1.status())
    planeta1.coletar_recursos(30)

    print(planeta2.status())
    planeta2.coletar_recursos(40)

    nave.viajar(planeta1)
    nave.carregar(50)
    nave.viajar(planeta2)
    nave.descarregar()

if __name__ == "__main__":
     main()