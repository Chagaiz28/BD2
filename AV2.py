from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import json

cloud_config= {
  'secure_connect_bundle': 'secure-connect-dbiot.zip'
}


with open("dbiot-token.json") as f:
    secrets = json.load(f)

CLIENT_ID = secrets["clientId"]
CLIENT_SECRET = secrets["secret"]


auth_provider = PlainTextAuthProvider(
    CLIENT_ID,
    CLIENT_SECRET
)


cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)


session = cluster.connect()

session.execute("""use ksiot;""")

# questao 1
session.execute("""
CREATE TABLE IF NOT EXISTS estoque (
    id int PRIMARY KEY,
    nome text,
    carro text,
    estante int,
    nivel int,
    quantidade int
)
""")


session.execute("""
INSERT INTO estoque (id, nome, carro, estante, nivel, quantidade) VALUES (5, 'Pistao', 'Mustang', 4, 1, 167)
""")


session.execute("""
INSERT INTO estoque (id, nome, carro, estante, nivel, quantidade) VALUES (4, 'Suspencao', 'Argo', 1, 1, 3500)
""")


# Questão 2

pistao = session.execute("SELECT * FROM estoque WHERE nome = 'Pistao' ALLOW FILTERING").all()
print(pistao)


media = session.execute("SELECT AVG(quantidade) FROM estoque").one()
print(media)

count = session.execute("SELECT COUNT(*) FROM estoque").one()
print(count)


quantidades = session.execute("SELECT MAX(quantidade) AS maior_quantidade, MIN(quantidade) AS menor_quantidade FROM estoque").one()
print(quantidades)


atributos = session.execute("SELECT nome, carro, quantidade FROM estoque WHERE estante = 3 ALLOW FILTERING").all()
print(atributos)

# Faça uma busca que retorne a média aritmética da quantidade onde o nível seja igual a 1;
media1 = session.execute("SELECT AVG(quantidade) FROM estoque WHERE nivel = 1 ALLOW FILTERING").one()
print(media1)


atributos = session.execute("SELECT * FROM estoque WHERE estante < 3 AND nivel > 4 ALLOW FILTERING").all()
print(atributos)

# Questão 3
carro = input("Digite o nome do carro: ")
atributos = session.execute(f"SELECT nome, estante, quantidade FROM estoque WHERE carro = '{carro}' ALLOW FILTERING").all()
print(atributos)


