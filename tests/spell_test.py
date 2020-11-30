import unittest
from db.run_sql import run_sql
from models.spell import Spell
import repositories.spell_repository as spell_repository
from models.wizard import Wizard
import repositories.wizard_repository as wizard_repository

class TestSpell(unittest.TestCase):
    def setUp(self):
        self.wizard = Wizard("Norman", "Stargazer", 1000)
        self.spell = Spell("I Wander", "Sudden, Unquenchable Wanderlust", self.wizard)
        
    # @unittest.skip("Delete this line to run the test")
    def test_spell_has_name(self):
        self.assertEqual("I Wander", self.spell.name)

