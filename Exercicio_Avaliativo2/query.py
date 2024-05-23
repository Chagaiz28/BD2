from database import Database

db = Database("bolt://18.234.76.182:7687", "neo4j", "weed-parties-battleship") 

def query_teacher_renzo():
    query = "MATCH (t:Teacher) WHERE t.name = 'Renzo' RETURN t.ano_nasc, t.CPF"
    return db.execute_query(query)

def query_teachers_starting_with_m():
    query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name, t.cpf"
    return db.execute_query(query)

def query_all_cities():
    query = "MATCH (c:City) RETURN c.name"
    return db.execute_query(query)

def query_schools_between_150_and_550():
    query = "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name, s.address, s.number"
    return db.execute_query(query)

def query_youngest_and_oldest_teacher():
    query_youngest = "MATCH (t:Teacher) RETURN t.ano_nasc ORDER BY t.ano_nasc DESC LIMIT 1"
    query_oldest = "MATCH (t:Teacher) RETURN t.ano_nasc ORDER BY t.ano_nasc ASC LIMIT 1"
    youngest = db.execute_query(query_youngest)
    oldest = db.execute_query(query_oldest)
    return youngest, oldest

def query_average_city_population():
    query = "MATCH (c:City) RETURN avg(c.population)"
    return db.execute_query(query)

def query_city_with_specific_zip():
    query = "MATCH (c:City) WHERE c.CEP = '37540-000' RETURN replace(c.name, 'a', 'A')"
    return db.execute_query(query)

def query_teacher_name_substring():
    query = "MATCH (t:Teacher) RETURN substring(t.name, 2)"
    return db.execute_query(query)