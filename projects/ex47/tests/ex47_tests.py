from ex47.game import Room
import unittest


class TestGame(unittest.TestCase):
    def test_room(self):
        gold = Room("GoldRoom", "this room has gold")
        self.assertEqual(gold.name, "GoldRoom")
