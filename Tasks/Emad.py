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


def add(first_num, second_num):
    if (type(first_num) == int or type(first_num) == float) and (type(second_num) == int or type(second_num) == float):
        return first_num+second_num
    else:
        return "Error: invalid input"


def divide(first_num, second_num):
    if (type(first_num) == int or type(first_num) == float) and (type(second_num) == int or type(second_num) == float):
        if(second_num == 0): return "undefined"
        return first_num//second_num
    else:
        return "Error: invalid input"

def sum_arr(arr):
    sum=0
    for num in arr:
        if (type(num) == int or type(num) == float):
            sum += num
        else:
            return "Error: invalid input"
    return sum



def even_list(list):
    evenlist = []
    for num in list:
        if (type(num) == int or type(num) == float) and num % 2 == 0:
            evenlist.append(int(num))
    return evenlist


class TestTasks(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, -2), -3)
        self.assertEqual(add(6, -5), 1)
        self.assertEqual(add('a', 1), "Error: invalid input")
        self.assertEqual(add(1, 'a'), "Error: invalid input")

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(-1, -1), 1)
        self.assertEqual(divide(7, 2), 3)
        self.assertEqual(divide(5, 0), "undefined")
        self.assertEqual(divide(5, 'a'), "Error: invalid input")
        self.assertEqual(divide('a', 1), "Error: invalid input")

    def test_sum_arr(self):
        self.assertEqual(sum_arr([1, 2, 3]), 6)
        self.assertEqual(sum_arr([0, 5, -3, -2]), 0)
        self.assertEqual(sum_arr(['a', 1, 'b']), "Error: invalid input")

    def test_even_list(self):
        self.assertEqual(even_list([1, 2, 3, 4]), [2, 4])
        self.assertEqual(even_list([0, 6, 12]), [0, 6, 12])
        self.assertEqual(even_list([9, 5, 3]), [])
        self.assertEqual(even_list(['a', 4, 'b']), [4])
        self.assertEqual(even_list(['a', 'c', 'b']), [])

if __name__ == '__main__':
    unittest.main()
