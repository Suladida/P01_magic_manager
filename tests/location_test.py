import unittest
from db.run_sql import run_sql
from models.location import Location
import repositories.location_repository as location_repository

class TestLocation(unittest.TestCase):
    def setUp(self):
        self.location = Location("Kilt Rock", "Natural Wonder", "Isle of Skye")
        
    # @unittest.skip("Delete this line to run the test")
    def test_location_has_realm(self):
        self.assertEqual("Isle of Skye", self.location.realm)

