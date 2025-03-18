from database import Database

class ProductAnalyzer:
    def __init__(self, database_name="mercado", collection_name="compras"):
        self.db = Database(database=database_name, collection=collection_name)

    def total_vendas_por_dia(self):
        """Retorna o total de vendas por dia."""
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$data_compra", "total_vendas": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}}
        ])
        return list(result)

    def produto_mais_vendido(self):
        """Retorna o produto mais vendido em todas as compras."""
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "quantidade_total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"quantidade_total": -1}},
            {"$limit": 1}
        ])
        return list(result)

    def cliente_que_mais_gastou(self):
        """Encontra o cliente que mais gastou em uma única compra."""
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id", "total_gasto": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total_gasto": -1}},
            {"$limit": 1}
        ])
        return list(result)

    def produtos_vendidos_acima_de_1_unidade(self):
        """Lista todos os produtos que tiveram uma quantidade vendida acima de 1 unidade."""
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "quantidade_total": {"$sum": "$produtos.quantidade"}}},
            {"$match": {"quantidade_total": {"$gt": 1}}}
        ])
        return list(result)
