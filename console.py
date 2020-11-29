import pdb

from models.wizard import Wizard
# from models.location import Location

import repositories.wizard_repository as wizard_repository
# import repositories.location_repository as location_repository

# wizard_repository.delete_all() 

wizard1 = Wizard("Gandalferoo", "DePurple", "3000")
wizard_repository.save(wizard1)
wizard2 = Wizard("Merlin", "McSpells", "1500")
wizard_repository.save(wizard2)

wizards = wizard_repository.select_all()

pdb.set_trace()
