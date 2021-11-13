import unittest

from markov import create_dictionary

class TestMarkov(unittest.TestCase):

    def test_sample(self):
        filename = 'sample.txt'        
        actual = create_dictionary(filename)
        expected = {
            'A': ['B', 'B', 'C.'], 
            'C': ['C', 'C.'],
            'B': ['A.', 'C.', 'A'], 
            '$': ['A', 'A', 'B', 'C']
        }

        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()