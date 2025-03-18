from ProductAnalyzer import ProductAnalyzer
from helper.writeAJson import writeAJson
from database import Database

db = Database(database="mercado", collection="compras")
db.resetDatabase()  # Descomente essa linha para popular os dados

# Criando a instância do analisador
analyzer = ProductAnalyzer()

# 1. Total de vendas por dia
vendas_por_dia = analyzer.total_vendas_por_dia()
print("\n📊 Total de vendas por dia:")
for item in vendas_por_dia:
    print(f"Data: {item['_id']}, Total de Vendas: R$ {item['total_vendas']:.2f}")
writeAJson(vendas_por_dia, "Total de vendas por dia")

# 2. Produto mais vendido
produto_mais_vendido = analyzer.produto_mais_vendido()
print("\n🏆 Produto mais vendido:")
for item in produto_mais_vendido:
    print(f"Produto: {item['_id']}, Quantidade vendida: {item['quantidade_total']}")
writeAJson(produto_mais_vendido, "Produto mais vendido")

# 3. Cliente que mais gastou
cliente_top = analyzer.cliente_que_mais_gastou()
print("\n💰 Cliente que mais gastou em uma única compra:")
for item in cliente_top:
    print(f"Cliente ID: {item['_id']}, Total gasto: R$ {item['total_gasto']:.2f}")
writeAJson(cliente_top, "Cliente que mais gastou")

# 4. Produtos vendidos acima de 1 unidade
produtos_acima_de_um = analyzer.produtos_vendidos_acima_de_1_unidade()
print("\n🛒 Produtos vendidos acima de 1 unidade:")
for item in produtos_acima_de_um:
    print(f"Produto: {item['_id']}, Quantidade total vendida: {item['quantidade_total']}")
writeAJson(produtos_acima_de_um, "Produtos vendidos acima de 1 unidade")
