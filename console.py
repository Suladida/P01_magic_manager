import pdb

from models.wizard import Wizard
from models.location import Location
from models.spell import Spell
from models.cast import Cast

import repositories.wizard_repository as wizard_repository
import repositories.location_repository as location_repository
import repositories.spell_repository as spell_repository
import repositories.cast_repository as cast_repository

cast_repository.delete_all()
spell_repository.delete_all() 
wizard_repository.delete_all() 
location_repository.delete_all() 

wizard1 = Wizard("Gandalferoo", "DePurple", 2000)
wizard_repository.save(wizard1)
wizard2 = Wizard("Merlin", "McSpells", 1500)
wizard_repository.save(wizard2)
wizard3 = Wizard("Captain", "Magicpants", 200)
wizard_repository.save(wizard3)

location1 = Location("Asda", "Supermarket", "Mordor")
location_repository.save(location1)
location2 = Location("Arthur's Seat", "Natural Wonder", "Edinburgh")
location_repository.save(location2)

spell1 = Spell("Ripe Old Mage", "Age Acceleration", wizard1)
spell_repository.save(spell1)
spell2 = Spell("Spell The Beans", "Relentless Honesty", wizard2)
spell_repository.save(spell2)
spell3 = Spell("Wiccapedia", "Downloads entire Wikipedia server to brain, explosion.", wizard2)
spell_repository.save(spell3)

cast1 = Cast(5,"5 People Aged Beyond Saving", wizard2, spell1, location1)
cast_repository.save(cast1)

locations = location_repository.select_all()
wizards = wizard_repository.select_all()
spells = spell_repository.select_all()
casts = cast_repository.select_all()

# Testing Update Wizard (Change Age)
wizard_update = Wizard("Gandalferoo", "DePurple", 3000, wizard1.id)
wizard_repository.update(wizard_update)

# Testing Update Spell (Changed Wizard)
spell_update = Spell("Spell The Beans", "Relentless Honesty", wizard3, spell1.id)
spell_repository.update(spell_update)

# Testing Update Location (Changed Supermarket Name)
location_update = Location("Lidl", "Supermarket", "Mordor", location1.id)
location_repository.update(location_update)

# Testing Update Cast (Changed Deaths and Location)
cast_update = Cast(10,"5 People Aged Beyond Saving", wizard2, spell1, location2, cast1.id)
cast_repository.update(cast_update)

pdb.set_trace()
