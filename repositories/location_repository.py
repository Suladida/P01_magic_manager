from db.run_sql import run_sql
from models.location import Location
import repositories.location_repository as location_repository

# CREATE:
# save function goes here
def save(location):
    sql = "INSERT INTO locations (name, type, realm) VALUES (%s, %s, %s) RETURNING *"
    values = [location.name, location.type, location.realm]
    results = run_sql(sql, values)
    id = results[0]['id']
    location.id = id
    return location

# READ_ALL:
# select_all function goes here
def select_all():
    locations = []

    sql = "SELECT * FROM locations"
    results = run_sql(sql)

    for row in results:
        location = Location(row['name'], row['type'], row['realm'], row['id'] )
        locations.append(location)
    return locations

# READ:
# select function goes here
def select(id):
    location = None
    sql = "SELECT * FROM locations WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        location = Location(result['name'], result['type'], result['realm'], result['id'] )
    return location

# UPDATE:
# - update function goes here
def update(location):
    sql = "UPDATE locations SET (name, type, realm) = (%s, %s, %s) WHERE id = %s"
    values = [location.name, location.type, location.realm, location.id]
    run_sql(sql, values)
    print(f"✅ Location Updated: {location.id} {location.name} {location.type} {location.realm}")

# DELETE:
# - delete function goes here
def delete(id):
    sql = "DELETE FROM locations WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# DELETE_ALL:
# - delete_all function goes here
def delete_all():
    sql = "DELETE FROM locations"
    run_sql(sql)

# SHOW ALL CASTS
# - location_casts function goes here

# SHOW ALL WIZARDS
# - location_wizards function goes here

# SHOW ALL SPELLS
# - location_spells function goes here

# TOTAL DEATHS
# - location_deaths function goes here
