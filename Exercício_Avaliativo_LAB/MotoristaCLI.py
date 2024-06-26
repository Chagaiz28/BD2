from MotoristaDAO import MotoristaDAO


class MotoristaCLI:
    def __init__(self, motorista_dao: MotoristaDAO):
        self.motorista_dao = motorista_dao

    def create_motorista(self):
        nome = input("Digite o nome do motorista: ")
        nota = float(input("Digite a nota do motorista: "))

        corridas = []
        while True:
            nota_corrida = int(input("Digite a nota da corrida: "))
            distancia = float(input("Digite a distância da corrida: "))
            valor = float(input("Digite o valor da corrida: "))
            nome_passageiro = input("Digite o nome do passageiro: ")
            documento_passageiro = input("Digite o documento do passageiro: ")

            # Criando um dicionário com os dados da corrida e do passageiro
            passageiro = {"nome": nome_passageiro, "documento": documento_passageiro}
            corrida = {"nota": nota_corrida, "distancia": distancia, "valor": valor, "passageiro": passageiro}
            corridas.append(corrida)

            continuar = input("Deseja adicionar outra corrida? (s/n): ")
            if continuar.lower() != "s":
                break

        # Criando um dicionário com os dados do motorista, incluindo as corridas
        motorista = {"nome": nome, "nota": nota, "corridas": corridas}

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
