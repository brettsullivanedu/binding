import unittest
import math

# Assuming the functions are defined in a file named school_subjects.py
# from school_subjects import calculate_area_of_circle, celsius_to_kelvin, calculate_kinetic_energy

# Example functions directly included here for demonstration
def calculate_area_of_circle(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

def celsius_to_kelvin(temperature_celsius):
    if temperature_celsius < -273.15:
        raise ValueError("Temperature cannot be below absolute zero")
    return temperature_celsius + 273.15

def calculate_kinetic_energy(mass, velocity):
    if mass < 0 or velocity < 0:
        raise ValueError("Mass and velocity must be non-negative")
    return 0.5 * mass * velocity ** 2

class TestSchoolSubjects(unittest.TestCase):
    def test_calculate_area_of_circle(self):
        self.assertAlmostEqual(calculate_area_of_circle(5), math.pi * 25)
        self.assertEqual(calculate_area_of_circle(0), 0)
        with self.assertRaises(ValueError):
            calculate_area_of_circle(-1)

    def test_celsius_to_kelvin(self):
        self.assertEqual(celsius_to_kelvin(0), 273.15)
        self.assertEqual(celsius_to_kelvin(-273.15), 0)
        with self.assertRaises(ValueError):
            celsius_to_kelvin(-300)
    
    def test_calculate_kinetic_energy(self):
        self.assertEqual(calculate_kinetic_energy(10, 2), 20)
        self.assertEqual(calculate_kinetic_energy(0, 5), 0)
        with self.assertRaises(ValueError):
            calculate_kinetic_energy(-1, 10)

if __name__ == '__main__':
    unittest.main()
