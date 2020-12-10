"""
1. Write a function that sums two number.
2. Write a function that divides two numbers,
   but doesn't return a floating point value.
3. Write a function that sums a whole array of numbers.
4. Write a function that prints the even numbers from a given list.

---
Please note that:
1. Your functions should handle cases in which you don't
expect the same data type. In other words,
your first function should fail if you tried to sum two strings.

2. Your test cases should cover every case you can think off.
"""

import unittest

ERROR_MASSAGE_INVALID_DATATYPE = 'Error with data type'
ERROR_MASSAGE_UNDEFINED_DIVISION = 'Undefined division'


def is_int_or_float(numbers):
    return all(isinstance(number, (int, float)) for number in numbers)


def divide_two_numbers(numerator, denominator):
    if not is_int_or_float([numerator, denominator]):
        return ERROR_MASSAGE_INVALID_DATATYPE
    try:
        return numerator // denominator
    except ZeroDivisionError:
        return ERROR_MASSAGE_UNDEFINED_DIVISION


divide_two_numbers.__doc__ = "function that divide two numbers"


def sum_numbers(numbers):
    if not is_int_or_float(numbers):
        return ERROR_MASSAGE_INVALID_DATATYPE
    return sum(numbers)


sum_numbers.__doc__ = "function that sum list of numbers"


def sum_two_numbers(first_number, second_number):
    if not is_int_or_float([first_number, second_number]):
        return ERROR_MASSAGE_INVALID_DATATYPE
    return first_number + second_number


sum_two_numbers.__doc__ = "function that sum two numbers"


def print_even_numbers(numbers):
    print([number for number in numbers if number % 2 == 0])


sum_two_numbers.__doc__ = "function print even numbers form given list"


class Test(unittest.TestCase):
    # TODO handle pass whole datatype in python
    def test_is_int_or_float(self):
        pass

    def test_divide_two_numbers(self):
        self.assertEqual(divide_two_numbers(6, 4), 1)
        self.assertEqual(divide_two_numbers(-1, -1), 1)
        self.assertEqual(divide_two_numbers(5, 6), 0)
        self.assertEqual(divide_two_numbers(1, 4), 0)
        self.assertEqual(divide_two_numbers(80, 8), 10)
        self.assertEqual(divide_two_numbers(79, 8), 9)
        self.assertEqual(divide_two_numbers(74, 0), ERROR_MASSAGE_UNDEFINED_DIVISION)
        self.assertEqual(divide_two_numbers(74, 'fy el gana'), ERROR_MASSAGE_INVALID_DATATYPE)

    def test_sum_numbers(self):
        self.assertEqual(sum_numbers([3, 0, 3]), 6)
        self.assertEqual(sum_numbers([-1, -1, 0]), -2)
        self.assertEqual(sum_numbers([10000, 10000, 10000]), 30000)
        self.assertEqual(sum_numbers([-10000000, 10000000, 10000000]), 10000000)
        self.assertEqual(sum_numbers([2.3, 2.3, 0, 5]), 9.6)
        self.assertEqual(sum_numbers([8.1, 8.1, 10.3]), 26.5)
        self.assertEqual(sum_numbers([1, 2, 'lol']), ERROR_MASSAGE_INVALID_DATATYPE)

    def test_sum_two_numbers(self):
        self.assertEqual(sum_two_numbers(10, 5), 15)
        self.assertEqual(sum_two_numbers(-1, 1), 0)
        self.assertEqual(sum_two_numbers(2.3, 2.3), 4.6)
        self.assertEqual(sum_two_numbers(1000, 5), 1005)
        self.assertEqual(sum_two_numbers("yahia", -1), ERROR_MASSAGE_INVALID_DATATYPE)

    # TODO How we test void function
    def test_print_even_numbers(self):
        pass


if __name__ == '__main__':
    unittest.main()
