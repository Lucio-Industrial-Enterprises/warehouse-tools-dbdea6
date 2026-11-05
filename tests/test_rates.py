import unittest

from warehouse.rates import shipping_quote


class RateTests(unittest.TestCase):
    def test_standard_rates(self):
        self.assertEqual(shipping_quote(2, "local"), 8.0)
        self.assertEqual(shipping_quote(2, "regional"), 11.0)

    def test_local_base_charge(self):
        for weight in (0.5, 1, 3):
            with self.subTest(weight=weight):
                self.assertEqual(shipping_quote(weight, "local"), 5.0 + 1.5 * weight)

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local")
