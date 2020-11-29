from db.run_sql import run_sql
from models.wizard import Wizard
import repositories.wizard_repository as wizard_repository

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

# READ:
# select function goes here

# UPDATE:
# - update function goes here

# DELETE:
# - delete function goes here

# DELETE_ALL:
# - delete_all function goes here