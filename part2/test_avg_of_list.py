import avg_of_list
import unittest

class Case(unittest.TestCase):
    def test_average_list(self):
        lst = [1, 1, 1, 1, 1]
        results = avg_of_list.average(lst)
        self.assertEqual(results, 1)

    def test_average_list_empty(self):
        lst = []
        self.assertRaises(Exception, avg_of_list.average, lst)

    def test_average_list_not_numbers(self):
        lst = ['jg', 'fj', 'aS', 'sdfg']
        self.assertRaises(Exception, avg_of_list.average, lst)
