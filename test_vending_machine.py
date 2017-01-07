import unittest
from vending_machine import give_change



class TestVendingMachine(unittest.TestCase):
    def test_return_change(self):
        self.assertEqual(give_change(17), [10, 5, 2], 'wrong change given')
        self.assertEqual(give_change(18), [10, 5, 2, 1], 'wrong change given')