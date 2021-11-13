import unittest

from markov import create_dictionary
from markov import create_sentence_list


class TestSentenceList(unittest.TestCase):

    def test_1(self):
        filename = 'sample.txt'
        actual = create_sentence_list('sample.txt')
        expected = ['A B A.' 'A B C.' 'B A C.' 'C C C.']

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

        self.assertEqual(actual['$'], expected['$'])
        self.assertEqual(actual['A'], expected['A'])
        self.assertEqual(actual, expected)

    def test_simple(self):        
        filename = 'simple.txt'        
        actual = create_dictionary(filename)
        expected = {
            '$': ['ROMEO'],
            'ROMEO': ['AND']
        }

        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()