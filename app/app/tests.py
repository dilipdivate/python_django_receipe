"""Sample test"""

from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):
  """Test the Calc module"""
  def test_add_numbers(self):
    """Test adding numbers together"""
    res = calc.add(2,3)
    self.assertEqual(res, 5)

  def test_subtract_numbers(self):
    """Test adding numbers together"""
    res = calc.subtract(7,3)
    self.assertEqual(res, 4)
        