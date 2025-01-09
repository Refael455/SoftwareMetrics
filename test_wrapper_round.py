"""This module allows to do unitary tests"""

import unittest
from aharouni_refael_software_metrics_final_exam import wrapper_round


class TestRoundNumber(unittest.TestCase):
    """This class contains the unitary tests for wrapper_round"""

    def test_positive_number(self):
        """This function tests the case where x is a positive number"""
        self.assertEqual(wrapper_round(2.34567), 2.3)

    def test_zero(self):
        """This function tests the case where x is zero"""
        self.assertEqual(wrapper_round(0), 0.0)

    def test_negative_number(self):
        """This function tests the case where x is a negative number"""
        self.assertEqual(wrapper_round(-18.96), -19)

    def test_edge_upper_positive_case(self):
        """This function tests an edge case (x positive)"""
        self.assertEqual(wrapper_round(1.05), 1.1)

    def test_edge_lower_positive_case(self):
        """This function tests an edge case (x positive)"""
        self.assertEqual(wrapper_round(1.04), 1.0)

    def test_edge_upper_negative_case(self):
        """This function tests an edge case (x negative)"""
        self.assertEqual(wrapper_round(-4.05), -4.0)

    def test_edge_lower_negative_case(self):
        """This function tests an edge case (x negative)"""
        self.assertEqual(wrapper_round(-12.14), -12.1)

    def test_integer_positive_case(self):
        """This function tests the case: x is in |N"""
        self.assertEqual(wrapper_round(5.0), 5)

    def test_integer_negative_case(self):
        """This function tests the case: x is in |Z"""
        self.assertEqual(wrapper_round(-5.0), -5)

    def test_extreme_case(self):
        """This function tests a case where x tends to zero"""
        self.assertEqual(wrapper_round(1.000001), 1.0)

    def test_one_decimal(self):
        """This function tests the case with one number in the decimal part"""
        self.assertEqual(wrapper_round(1.5), 1.5)

    def test_not_a_decimal_number(self):
        """This function tests the case where x is a string"""
        with self.assertRaises(ValueError):
            wrapper_round("shjkf")


if __name__ == '__main__':
    unittest.main()
