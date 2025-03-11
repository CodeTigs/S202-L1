from database import Database
from helper.writeAJson import writeAJson


class Pokedex:
    def __init__(self, database: Database):
        self.database = database  # Correção no acesso ao banco de dados

    def get_pokemon_by_name(self, name: str):
        """Consulta um Pokémon pelo nome."""
        resposta = self.database.collection.find_one({"name": name})
        writeAJson(resposta, f"pokemon_{name}")
        return resposta

    def get_pokemon_by_type(self, pokemon_type: str):
        """Consulta Pokémon por tipo (ex: 'Fire', 'Water')."""
        resposta = list(self.database.collection.find({"type": pokemon_type}))
        writeAJson(resposta, f"pokemons_type_{pokemon_type}")
        return resposta

    def get_pokemon_by_weakness(self, weakness: str):
        """Consulta Pokémon vulneráveis a um determinado tipo."""
        resposta = list(self.database.collection.find({"weaknesses": {"$in": [weakness]}}))
        writeAJson(resposta, f"pokemons_weakness_{weakness}")
        return resposta

    def get_pokemon_by_candy_count(self, min_candy: int, max_candy: int):
        """Consulta Pokémon que exigem um número mínimo de candies para evoluir."""
        resposta = list(self.database.collection.find({"candy_count": {"$gte": min_candy, "$lte": max_candy}}))
        writeAJson(resposta, f"pokemons_candy_{min_candy}_to_{max_candy}")
        return resposta
    
    def get_pokemon_by_spawn_time(self, spawn_time: str):
        """Consulta Pokémon que aparecem em determinado horário."""
        resposta = list(self.database.collection.find({"spawn_time": spawn_time}))
        writeAJson(resposta, f"pokemons_spawn_{spawn_time.replace(':', '')}")
        return resposta


# Teste da Pokedex
if __name__ == "__main__":
    db = Database(database="pokedex", collection="pokemons")
    pokedex = Pokedex(db)

    # Executando consultas de exemplo
    pokedex.get_pokemon_by_name("Pikachu")
    pokedex.get_pokemon_by_type("Fire")
    pokedex.get_pokemon_by_weakness("Water")
    pokedex.get_pokemon_by_candy_count(10, 50)
    pokedex.get_pokemon_by_spawn_time("04:00")
