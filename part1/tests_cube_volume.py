import cube_volume
import unittest

class Case(unittest.TestCase):
    def test_calculate_volume_correct_value(self):
        result = cube_volume.calculate_volume(5, 4, 6)
        self.assertEqual(result, 120)

        result = cube_volume.calculate_volume(4, 5, '5')
        self.assertEqual(result, 100)

    def test_calcualte_volume_negative_number(self):
        self.assertRaises(Exception, cube_volume.calculate_volume, 5, -4, 5)


    def test_calculate_volume_non_number(self):
        self.assertRaises(Exception, cube_volume.calculate_volume, 'hj', 5, 4)
        self.assertRaises(Exception, cube_volume.calculate_volume, 'hj', 'k', 'kj')
        self.assertRaises(Exception, cube_volume.calculate_volume, 'hj', 5, 4)


    def test_calculate_voume_zero_input(self):
        self.assertRaises(Exception, cube_volume.calculate_volume, 5, 4, 0)
        self.assertRaises(Exception, cube_volume.calculate_volume, 5, 0, 0)
        self.assertRaises(Exception, cube_volume.calculate_volume, 0, 0, 0)
        self.assertRaises(Exception, cube_volume.calculate_volume, 0, 4, 0)
        self.assertRaises(Exception, cube_volume.calculate_volume, 0, 0, 6)
        self.assertRaises(Exception, cube_volume.calculate_volume, 0, 5, 3)
