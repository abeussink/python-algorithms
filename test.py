import unittest
import makechange

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        change = makechange.make_change_greedy(65)
        self.assertEqual(change, ['quarter', 'quarter', 'dime', 'nickel'])
        
if __name__ == '__main__':
    unittest.main()