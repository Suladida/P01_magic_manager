import unittest
from db.run_sql import run_sql
from models.location import Location
import repositories.location_repository as location_repository
from models.spell import Spell
import repositories.spell_repository as spell_repository
from models.wizard import Wizard
import repositories.wizard_repository as wizard_repository
from models.cast import Cast
import repositories.cast_repository as cast_repository 


class TestCast(unittest.TestCase):
    def setUp(self):
        self.cast = Cast(7, "Magical Explosion", 1,2,3)

    # @unittest.skip("Delete this line to run the test")
    def test_spell_has_deaths(self):
        self.assertEqual(7, self.cast.deaths)

