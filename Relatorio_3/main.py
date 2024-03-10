from database import Database
from helper.writeAJson import writeAJson
from pokedex import Pokedex

db = Database(database="pokedex", collection="pokemons")

pokedex_instance = Pokedex(database=db)

pokedex_instance.query_pokemon_by_id(1)
pokedex_instance.query_pokemon_by_name("Bulbasaur")
pokedex_instance.query_pokemon_by_type("Grass")
pokedex_instance.query_pokemon_by_weakness("Fire")
pokedex_instance.query_pokemon_by_spawn_chance(0.69)

db.resetDatabase()