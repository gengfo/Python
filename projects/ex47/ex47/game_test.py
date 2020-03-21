import unittest
from game import Room

class RoomTest(unittest.TestCase):
    def test_room(self):
        room = Room("a", "b")
        self.assertEqual("a", room.name)
