import unittest

from markov import create_dictionary
from markov import create_sentence_list


class TestSentenceList(unittest.TestCase):

    def test_sample(self):
        filename = 'sample.txt'
        actual = create_sentence_list(filename)
        expected = ['A B A.', 'A B C.', 'B A C.', 'C C C.']

        self.assertEqual(actual, expected)

    def test_edited_mission(self):
        filename = 'edited_mission.txt'
        actual = create_sentence_list(filename)
        expected = [
            'Boston University is a comprehensive university.',
            'It is committed to educating students to be ready to live and to lead in an interconnected world.',
            'It is committed to generating new knowledge.',
            'It is amazing!'
        ]

        print('ACTUAL: {}'.format(actual))

        self.assertEqual(actual, expected)

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

    def test_edited_mission(self):
        self.maxDiff = None
        filename = 'edited_mission.txt'        
        actual = create_dictionary(filename)
        expected = {
            'a': ['comprehensive'],
            'be': ['ready'],
            'and': ['to'],
            'in': ['an'],
            '$': ['Boston', 'It', 'It', 'It'],
            'lead': ['in'],
            'educating': ['students'],
            'students': ['to'],
            'Boston': ['University'],
            'University': ['is'],
            'committed': ['to', 'to'],
            'generating': ['new'],
            'It': ['is', 'is', 'is'],
            'an': ['interconnected'],
            'to': ['educating', 'be', 'live', 'lead', 'generating'],
            'live': ['and'],
            'comprehensive': ['university.'],
            'ready': ['to'],
            'new': ['knowledge.'],
            'interconnected': ['world.'],
            'is': ['a', 'committed', 'committed', 'amazing!']
        }

        self.assertEqual(actual['a'], expected['a'])
        self.assertEqual(actual['be'], expected['be'])
        self.assertEqual(actual['and'], expected['and'])
        self.assertEqual(actual['$'], expected['$'])

        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()