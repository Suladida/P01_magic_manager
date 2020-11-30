from db.run_sql import run_sql
from models.spell import Spell
from models.wizard import Wizard
import repositories.spell_repository as spell_repository
import repositories.wizard_repository as wizard_repository

# CREATE:
# save function goes here
def save(spell):
    sql = "INSERT INTO spells (name, description, wizard_id) VALUES (%s, %s, %s) RETURNING *"
    values = [spell.name, spell.description, spell.wizard.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    spell.id = id
    return spell

# READ_ALL:
# select_all function goes here
def select_all():
    spells = []

    sql = "SELECT * FROM spells"
    results = run_sql(sql)

    for row in results:
        wizard = wizard_repository.select(row['wizard_id'])
        spell = Spell(row['name'], row['description'], wizard, row['id'] )
        spells.append(spell)
    return spells

# READ:
# select function goes here
def select(id):
    spell = None
    sql = "SELECT * FROM spells WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        wizard = wizard_repository.select(result['wizard_id'])
        spell = Spell(result['name'], result['description'], wizard, result['id'] )
    return spell

# UPDATE:
# - update function goes here
def update(spell):
    sql = "UPDATE spells SET (name, description, wizard_id) = (%s, %s, %s) WHERE id = %s"
    values = [spell.name, spell.description, spell.wizard.id, spell.id]
    run_sql(sql, values)
    print(f"✅ Spell Updated: {spell.name} {spell.description} {spell.wizard.id} {spell.id}")

# DELETE:
# - delete function goes here
def delete(id):
    sql = "DELETE FROM spells WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# DELETE_ALL:
# - delete_all function goes here
def delete_all():
    sql = "DELETE FROM spells"
    run_sql(sql)

# SHOW ALL CASTS
# - spell_casts function goes here

# SHOW ALL LOCATIONS
# - location_spells function goes here

# SHOW ALL WIZARDS
# - assigned_wizards function goes here

# TOTAL DEATHS
# - total_deaths function goes here
