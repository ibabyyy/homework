import unittest
from plus import plus1

class Testplus(unittest, TestCase):
    def test_plus(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(4, 7), 11)

    def test_plus_floats(self):
        self.assertAlmostEqual(add(2.5, 5.2), 7.7)


if __name__ == "__main__":
    unittest.main()