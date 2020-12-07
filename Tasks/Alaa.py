import unittest


def is_valid_data_type(value):
    if type(value) != int and type(value) != float:
        return 0
    else:
        return 1


def divide_two_numbers(first_number, second_number):
    if is_valid_data_type(first_number) and is_valid_data_type(second_number):
        if second_number == 0:
            return "Undefined"
        return first_number // second_number
    else:
        return "Error: can't divide these values"


def summation_of_array(numbers):
    sum = 0
    for number in numbers:
        if is_valid_data_type(number):
            sum += number
        else:
            return "Error : the array should contain only numbers"
    return sum


def sums_two_numbers(first_number, second_number):
    if is_valid_data_type(first_number) and is_valid_data_type(second_number):
        return first_number + second_number
    else:
        return "Error : only accept numbers"


def get_even_numbers(numbers):
    arr = []
    for number in numbers:
        if is_valid_data_type(number) and number % 2 == 0:
            arr.append(number)
    return arr


class TestTasks(unittest.TestCase):

    def test_sum_two_numbers(self):
        self.assertEqual(sums_two_numbers(10, 5), 15)
        self.assertEqual(sums_two_numbers(-1, 1), 0)
        self.assertEqual(sums_two_numbers(-1, -1), -2)
        self.assertEqual(sums_two_numbers("s", -1), "Error : only accept numbers")

    def test_summation_of_array(self):
        self.assertEqual(summation_of_array([1, 2, 3]), 6)
        self.assertEqual(summation_of_array([-1, 1, 0]), 0)
        self.assertEqual(summation_of_array([1, 2, 'x']), "Error : the array should contain only numbers")

    def test_divide_two_numbers(self):
        self.assertEqual(divide_two_numbers(10, 5), 2)
        self.assertEqual(divide_two_numbers(-1, 1), -1)
        self.assertEqual(divide_two_numbers(-1, -1), 1)
        self.assertEqual(divide_two_numbers(5, 2), 2)
        self.assertEqual(divide_two_numbers(5, 0), "Undefined")
        self.assertEqual(divide_two_numbers(5, 'x'), "Error: can't divide these values")

    def test_get_even_numbers(self):
        self.assertEqual(get_even_numbers([1, 2, 3]), [2])
        self.assertEqual(get_even_numbers([0, 2, 4]), [0, 2, 4])
        self.assertEqual(get_even_numbers([1, 1, -1]), [])
        self.assertEqual(get_even_numbers([2, 'x']), [2])

    def test_is_valid_data_type(self):
        self.assertTrue(is_valid_data_type(1))
        self.assertTrue(is_valid_data_type(1.25))
        self.assertFalse(is_valid_data_type('x'))


if __name__ == '__main__':
    unittest.main()
