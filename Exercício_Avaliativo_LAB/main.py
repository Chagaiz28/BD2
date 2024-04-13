from database import Database
from MotoristaCLI import MotoristaCLI
from MotoristaDAO import MotoristaDAO
def main():
    # Conectar ao banco de dados
    db = Database("BD", "Motoristas")

    motorista_dao = MotoristaDAO("BD", "Motoristas")

    # Instanciar o CLI do Motorista
    motorista_cli = MotoristaCLI(motorista_dao)

    # Executar o CLI do Motorista
    motorista_cli.run()

if __name__ == "__main__":
    main()
