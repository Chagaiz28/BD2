from pymongo import MongoClient
from bson.objectid import ObjectId

class LivroModel:
    def __init__(self, database):
        self.db = database

    def create_livro(self, titulo: str, autor: str, ano: int, preco: float):
        try:
            livro = {
                "titulo": titulo,
                "autor": autor,
                "ano": ano,
                "preco": preco
            }
            res = self.db.collection.insert_one(livro)
            print(f"Livro criado com ID: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar o livro: {e}")
            return None

    def read_livro_by_id(self, id: str):
        try:
            livro = self.db.collection.find_one({"_id": ObjectId(id)})
            if livro:
                print(f"Livro encontrado: {livro}")
            else:
                print("Livro não encontrado")
            return livro
        except Exception as e:
            print(f"Ocorreu um erro ao ler o livro: {e}")
            return None

    def update_livro(self, id: str, titulo: str, autor: str, ano: int, preco: float):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"titulo": titulo, "autor": autor, "ano": ano, "preco": preco}})
            if res.modified_count > 0:
                print(f"Livro atualizado com sucesso")
            else:
                print("Nenhum livro foi atualizado")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar o livro: {e}")
            return None

    def delete_livro(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            if res.deleted_count > 0:
                print(f"Livro excluído com sucesso")
            else:
                print("Nenhum livro foi excluído")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao excluir o livro: {e}")
            return None
