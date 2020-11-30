from db.run_sql import run_sql
from models.wizard import Wizard
from models.spell import Spell
from models.cast import Cast
import repositories.wizard_repository as wizard_repository
import repositories.spell_repository as spell_repository
import repositories.cast_repository as cast_repository

# CREATE:
# save function goes here
def save(wizard):
    sql = "INSERT INTO wizards (first_name, last_name, age) VALUES (%s, %s, %s) RETURNING *"
    values = [wizard.first_name, wizard.last_name, wizard.age]
    results = run_sql(sql, values)
    id = results[0]['id']
    wizard.id = id
    return wizard

# READ_ALL:
# select_all function goes here
def select_all():
    wizards = []

    sql = "SELECT * FROM wizards"
    results = run_sql(sql)

    for row in results:
        wizard = Wizard(row['first_name'], row['last_name'], row['age'], row['id'] )
        wizards.append(wizard)
    return wizards

# READ:
# select function goes here
def select(id):
    wizard = None
    sql = "SELECT * FROM wizards WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        wizard = Wizard(result['first_name'], result['last_name'], result['age'], result['id'] )
    return wizard

# UPDATE:
# - update function goes here
def update(wizard):
    sql = "UPDATE wizards SET (first_name, last_name, age) = (%s, %s, %s) WHERE id = %s"
    values = [wizard.first_name, wizard.last_name, wizard.age, wizard.id]
    run_sql(sql, values)
    print(f"✅ Wizard Updated: {wizard.id} {wizard.first_name} {wizard.last_name} {wizard.age}")

# DELETE:
# - delete function goes here
def delete(id):
    sql = "DELETE FROM wizards WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# DELETE_ALL:
# - delete_all function goes here
def delete_all():
    sql = "DELETE FROM wizards"
    run_sql(sql)

# SHOW ALL SPELLS:
# - function to show all spells will go here
def spells(wizard):
    spells = []

    sql = "SELECT * FROM spells WHERE wizard_id = %s"
    values = [wizard.id]
    results = run_sql(sql, values)

    for row in results:
        spell = Spell(row['name'], row['description'], row['wizard_id'], row['id'])
        spells.append(spell)
    return spells

def casts(wizard):
    casts = []

    sql = "SELECT * FROM casts WHERE wizard_id = %s"
    values = [wizard.id]
    results = run_sql(sql, values)

    for row in results:
        cast = Cast(row['deaths'], row['details'], row['wizard_id'], row['location_id'], row['spell_id'], row['id'],)
        casts.append(cast)
    return casts