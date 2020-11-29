from db.run_sql import run_sql
from models.cast import Cast
from models.wizard import Wizard
from models.spell import Spell
from models.location import Location
import repositories.cast_repository as cast_repository
import repositories.location_repository as location_repository
import repositories.spell_repository as spell_repository
import repositories.wizard_repository as wizard_repository

# CREATE:
# save function goes here
def save(cast):
    sql = "INSERT INTO casts (deaths, details, wizard_id, spell_id, location_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [cast.deaths, cast.details, cast.wizard.id, cast.spell.id, cast.location.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    cast.id = id
    return cast

# READ_ALL:
# select_all function goes here
def select_all():
    casts = []

    sql = "SELECT * FROM casts"
    results = run_sql(sql)

    for row in results:
        wizard = wizard_repository.select(row['wizard_id'])
        spell = spell_repository.select(row['spell_id'])
        location = location_repository.select(row['location_id'])
        cast = Cast(row['deaths'], row['details'], wizard, spell, location, row['id'] )
        casts.append(cast)
    return casts

# READ:
# select function goes here
def select(id):
    cast = None
    sql = "SELECT * FROM casts WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        wizard = wizard_repository.select(result['wizard_id'])
        spell = spell_repository.select(result['spell_id'])
        location = location_repository.select(result['location_id'])
        cast = Cast(result['deaths'], result['details'], wizard, spell, location, result['id'] )
    return cast

# UPDATE:
# - update function goes here
def update(cast):
    sql = "UPDATE casts SET (deaths, details, wizard, spell, location) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [cast.deaths, cast.details, cast.wizard.id, cast.spell.id, cast.location.id, cast.id]
    print(values)
    run_sql(sql, values)

# DELETE:
# - delete function goes here
def delete(id):
    sql = "DELETE FROM casts WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# DELETE_ALL:
# - delete_all function goes here
def delete_all():
    sql = "DELETE FROM casts"
    run_sql(sql)