from database import Database
from game_database import GameDatabase

db = Database("bolt://44.200.130.64:7687", "neo4j", "paints-stoppers-frigates")
db.drop_all()

game_db = GameDatabase(db)

game_db.create_player("player1", "Alice")
game_db.create_player("player2", "Bob")
game_db.create_match("match1", "Alice wins")
game_db.create_match("match2", "Bob wins")

game_db.add_player_to_match("player1", "match1")
game_db.add_player_to_match("player2", "match1")
game_db.add_player_to_match("player2", "match2")

game_db.update_player_name("player1", "Alice Smith")
game_db.update_match_result("match2", "Bob wins again")
