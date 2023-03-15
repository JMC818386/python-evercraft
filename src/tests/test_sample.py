# You can write tests here or create new files in this directory with the name test_[something].py
from character import Character

# Tests
# Create a Character
def test_create_character():
    c = Character('Bob', 'Good', "Heavy", "hp")
    assert isinstance(c, Character)

# Character has a name
def test_name_character():
    c = Character('Tim', 'Evil', "Heavy", "hp")
    assert hasattr(c, 'name')

# Character can set a name
def test_set_character_name():
    c = Character('Bill','Neutral', "Heavy", "hp")
    assert c.name == 'Bill'

# Character can have alignment
def test_character_alignment():
    c = Character('Dan', 'Neutral', "Heavy", "hp")
    assert hasattr(c, 'alignment')

# Character can be Neutral
def test_character_alignment():
    c = Character('Dan', 'Neutral', "Heavy", "hp")
    assert hasattr(c, 'alignment')

# Character can be Good
def test_create_character():
    c = Character('Bob', 'Good', "Heavy", "hp")
    assert hasattr(c, 'alignment')

# Character can be Evil
def test_name_character():
    c = Character('Tim', 'Evil', "Heavy", "hp")
    assert hasattr(c, 'alignment')

# Class for alignment?
def test_for_alignment():
    c = Character("Sam", "Good", "Heavy", "hp")
    assert hasattr(c, 'alignment')

# Character has armour attribute
def test_for_armour():
    c = Character("Sam", "Good", "Heavy", "hp")
    assert hasattr(c, 'armour')

# Character has hit points (hp) attribute
def test_for_hp():
    c = Character("Sam", "Good", "Heavy", "hp")
    assert hasattr(c, "hp")

# Character armour defaults to 10
# Hit hp defaults to 5
# Character needs to be able to attack another Character
# Character rolls a 20, attack succeeds
# Character rolls a 17, beat opp armour, attack succeeds
# Character rolls a 1, opp armour too much, attack fails
# Some sort of loop test to test for all rolls
# On successful attack, combatant loses hit point
# On roll = 20, critical hit dealt, attack x2
# Check hitpoints after successful attack, if < 0, dead
# Character has an attribute of alive: true