from ex47.game import Room
from nose.tools import *

def test_room():
    gold = Room("GoldRoom", "this room has gold")
    assert_equal(gold.name, "GoldRoom1")
