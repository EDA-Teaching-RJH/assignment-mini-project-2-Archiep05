import unittest
from utils.gym_library import calculate_total_weight, calculate_volume, kg_to_lbs, lbs_to_kg
from utils.validators import is_valid_name, is_valid_weight, is_valid_reps, is_valid_sets

class TestWeightCalculations(unittest.TestCase):
    def test_barbell_weight(self):
        self.assertEqual(calculate_total_weight(100, "barbell"), 100)
    
    def test_dumbbell_weight_doubles(self):
        self.assertEqual(calculate_total_weight(20, "dumbbell"), 40)
    
    def test_bodyweight(self):
        self.assertEqual(calculate_total_weight(0, "bodyweight", bodyweight=80), 80)
    
    def test_weighted_bodyweight(self):
        self.assertEqual(calculate_total_weight(10, "weighted_bodyweight", bodyweight=80), 90)
    
    def test_invalid_equipment(self):
        with self.assertRaises(ValueError):
            calculate_total_weight(100, "machine")
    
    def test_bodyweight_without_providing_bodyweight(self):
        with self.assertRaises(ValueError):
            calculate_total_weight(0, "bodyweight")

class TestVolumeCalculations(unittest.TestCase):
    def test_basic_volume(self):
        self.assertEqual(calculate_volume(3, 12, 100), 3600)
    
    def test_zero_reps(self):
        self.assertEqual(calculate_volume(3, 0, 100), 0)
    
    def test_zero_weight(self):
        self.assertEqual(calculate_volume(3, 10, 0), 0)