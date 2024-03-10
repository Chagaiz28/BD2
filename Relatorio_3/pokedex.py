from database import Database
from helper.writeAJson import writeAJson

class Pokedex:
    def __init__(self, database: Database):
        self.database = database

    def query_pokemon_by_id(self, pokemon_id):
        # Consulta um Pokémon pelo ID
        pokemon = self.database.collection.find_one({"id": pokemon_id})
        self.generate_logs(pokemon, f"pokemon_{pokemon_id}_query_log")

    def query_pokemon_by_name(self, pokemon_name):
        # Consulta um Pokémon pelo nome
        pokemon = self.database.collection.find_one({"name": pokemon_name})
        self.generate_logs(pokemon, f"pokemon_{pokemon_name}_query_log")

    def query_pokemon_by_type(self, pokemon_type):
        # Consulta Pokémon por tipo
        pokemons = self.database.collection.find({"type": pokemon_type})
        self.generate_logs(list(pokemons), f"pokemon_{pokemon_type}_type_query_log")

    def query_pokemon_by_weakness(self, weakness_type):
        # Consulta Pokémon por fraqueza
        pokemons = self.database.collection.find({"weaknesses": weakness_type})
        self.generate_logs(list(pokemons), f"pokemon_{weakness_type}_weakness_query_log")

    def query_pokemon_by_spawn_chance(self, spawn_chance):
        # Consulta Pokémon por chance de spawn
        pokemons = self.database.collection.find({"spawn_chance": spawn_chance})
        self.generate_logs(list(pokemons), f"pokemon_spawn_chance_{spawn_chance}_query_log")

    def generate_logs(self, data, name: str):
        # Gera logs utilizando a função writeAJson
        writeAJson(data, name)
