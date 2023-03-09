import unittest;
from Character import Character;

class CharacterTest(unittest.TestCase):

    def test_GetHpPercentage(self):
        char = Character();
        char.MAX_HP = 100;
        char.CURRENT_HP = 50;
        percentage = char.getHpPercentage();
        self.assertEqual(percentage, 0.5, "wrong hp percentage calculated");

unittest.main()