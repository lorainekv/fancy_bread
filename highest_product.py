import unittest
from operator import mul
from functools import reduce


def highest_product_of_3(list_of_ints):

    # Calculate the highest product of three numbers

    list_length = len(list_of_ints)
    # Short circuit
    if list_length < 3:
        raise Exception
    elif list_length == 3:
        return reduce(mul, list_of_ints)
    else:
        list_of_ints = sorted(list_of_ints, reverse=True)
        if (list_of_ints[-1] * list_of_ints[-2]) > (list_of_ints[0] * list_of_ints[1]):

            if list_of_ints[0] <= 0:
                # all are negative, multiply the largest ones
                product = reduce(mul, list_of_ints[0:3])
            else:
                product = (list_of_ints[-1] * list_of_ints[-2] * list_of_ints[0])
        else:
            product = reduce(mul, list_of_ints[0:3])

        return product

# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])

    def test_list_has_three_numbers(self):
        actual = highest_product_of_3([1, 3, 2])
        expected = 6
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
