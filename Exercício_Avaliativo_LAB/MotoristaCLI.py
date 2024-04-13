from MotoristaDAO import MotoristaDAO


class MotoristaCLI:
    def __init__(self, motorista_dao: MotoristaDAO):
        self.motorista_dao = motorista_dao

    def create_motorista(self):
        nome = input("Digite o nome do motorista: ")
        nota = float(input("Digite a nota do motorista: "))

        # Criando um dicionário com os dados do motorista
        motorista = {"nome": nome, "nota": nota}

        # Chamando o método de criar motorista da classe MotoristaDAO
        self.motorista_dao.criar_motorista(motorista)

    def read_motorista(self):
        id_motorista = input("Digite o ID do motorista: ")
        motorista = self.motorista_dao.ler_motorista({"_id": id_motorista})
        if motorista:
            print("Motorista encontrado:")
            print(motorista)
        else:
            print("Motorista não encontrado.")

    def update_motorista(self):
        id_motorista = input("Digite o ID do motorista que deseja atualizar: ")
        novos_dados = {}
        nome = input("Digite o novo nome do motorista (ou pressione Enter para manter o mesmo): ")
        if nome:
            novos_dados["nome"] = nome
        nota = input("Digite a nova nota do motorista (ou pressione Enter para manter a mesma): ")
        if nota:
            novos_dados["nota"] = float(nota)
        self.motorista_dao.atualizar_motorista({"_id": id_motorista}, novos_dados)

    def delete_motorista(self):
        id_motorista = input("Digite o ID do motorista que deseja excluir: ")
        self.motorista_dao.deletar_motorista({"_id": id_motorista})

    def run(self):
        print("Bem-vindo ao CLI do Motorista!")
        print("Comandos disponíveis: create, read, update, delete, quit")
        while True:
            command = input("Digite um comando: ")
            if command == "quit":
                print("Até logo!")
                break
            elif command == "create":
                self.create_motorista()
            elif command == "read":
                self.read_motorista()
            elif command == "update":
                self.update_motorista()
            elif command == "delete":
                self.delete_motorista()
            else:
                print("Comando inválido. Tente novamente.")
