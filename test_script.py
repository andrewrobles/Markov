import unittest

from script import return_0

class TestSolution(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(return_0(), 0)

if __name__ == '__main__':
    unittest.main()