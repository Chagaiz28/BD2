from database import Database
from helper.writeAJson import writeAJson

db = Database(database="mercado", collection="compras")
class ProductAnalyzer:
    def __init__(self, data):
        self.data = data

    def total_sales_per_day(self):
        result = db.collection.aggregate([
            {"$unwind" :  "$produtos"},
            {"$group" : {"_id" : "$data_compra", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}}
        ])
        writeAJson(result, "Total de Vendas por dia")


    def most_sold_product(self):
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ])
        writeAJson(result,"Produto mais vendido")

    def highest_spending_customer(self):
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group" : {"_id": "$cliente_id","total_gasto": { "$sum": { "$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total_gasto": -1}},
            {"$limit": 1}])
        writeAJson(result, "Cliente que mais gastou")

    def products_sold_above_one(self):
            result = db.collection.aggregate([
                {"$unwind" : "$produtos"},
                {"$match" : {"produtos.quantidade": { "$gt": 1}}},
                {"$group": {"_id": "$produtos.descricao","total_quantidade_vendida": { "$sum": "$produtos.quantidade"}}}])
            writeAJson(result, "Produtops vendidos mais que 1")

