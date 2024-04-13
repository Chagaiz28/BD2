from pymongo import MongoClient
from database import Database

class MotoristaDAO:
    def __init__(self, database: str, collection: str):
        self.db = Database(database, collection)

    def criar_motorista(self, motorista):
        try:
            self.db.collection.insert_one(motorista)
            print("Motorista criado com sucesso!")
        except Exception as e:
            print("Erro ao criar motorista:", e)

    def ler_motorista(self, filtro=None):
        try:
            if filtro:
                return self.db.collection.find_one(filtro)
            else:
                return list(self.db.collection.find())
        except Exception as e:
            print("Erro ao ler motorista:", e)
            return None

    def atualizar_motorista(self, filtro, novos_valores):
        try:
            self.db.collection.update_one(filtro, {"$set": novos_valores})
            print("Motorista atualizado com sucesso!")
        except Exception as e:
            print("Erro ao atualizar motorista:", e)

    def deletar_motorista(self, filtro):
        try:
            self.db.collection.delete_one(filtro)
            print("Motorista deletado com sucesso!")
        except Exception as e:
            print("Erro ao deletar motorista:", e)
