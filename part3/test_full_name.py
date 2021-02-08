import full_name
import unittest

class Case(unittest.TestCase):
    def test_generate_name(self):
        result = full_name.generate_name('Miles', 'Smith')
        self.assertEqual(result, 'Miles Smith')

    def test_generate_name_two_last_names(self):
        self.assertRaises(Exception, full_name.generate_name, 'Miles', 'Smith', 'Smith')

    def test_generate_name_no_last_name(self):
        self.assertRaises(Exception, full_name.generate_name, 'Miles')
