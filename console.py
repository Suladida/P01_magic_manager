import pdb

from models.wizard import Wizard
from models.location import Location
from models.spell import Spell

import repositories.wizard_repository as wizard_repository
import repositories.location_repository as location_repository
import repositories.spell_repository as spell_repository

spell_repository.delete_all() 
wizard_repository.delete_all() 
location_repository.delete_all() 

wizard1 = Wizard("Gandalferoo", "DePurple", 3000)
wizard_repository.save(wizard1)
wizard2 = Wizard("Merlin", "McSpells", 1500)
wizard_repository.save(wizard2)

location1 = Location("Asda", "Supermarket", "Mordor")
location_repository.save(location1)
location2 = Location("Arthur's Seat", "Natural Wonder", "Edinburgh")
location_repository.save(location2)

spell1 = Spell("Ripe Old Mage", "Age Acceleration", wizard1)
spell_repository.save(spell1)

locations = location_repository.select_all()
wizards = wizard_repository.select_all()
spells = spell_repository.select_all()

pdb.set_trace()
