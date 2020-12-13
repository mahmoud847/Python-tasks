# 1. Your functions should handle cases in which you don't
# expect the same data type. In other words,
# your first function should fail if you tried to sum two strings.
# Your test cases should cover every case you can think off.

import unittest

# 1. Write a function that sums two number.
def sum(x,y):
    if ( isinstance(x, (int, float)) and isinstance(y, (int, float))):
     return x+y
    else:
     return "invalid input"


# 2. Write a function that divides two numbers,
# but doesn't return a floating point value.
def divide(x, y):
    if (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        try:
         return x // y
        except ZeroDivisionError:
         return "invalid division"

    else:
        return "invalid input"


# 3. Write a function that sums a whole array of numbers.
def sumArray(arr):
    sum=0
    for i in arr:
     if (isinstance(i, (int, float))):
       sum += i
     else:
       return "invalid input"
    return sum


# 4. Write a function that prints the even numbers from a given list.
def evenArray(arr):
    arr2=[]
    for i in arr:
     if (isinstance(i, (int, float))):
         if(i % 2 == 0 and i!=0):
          arr2.append(i)
     else:
       return "invalid input"
    return arr2


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(sum(10, 5), 15)
        self.assertEqual(sum(-1, 1), 0)
        self.assertEqual(sum(-1, -1), -2)
        self.assertEqual(sum("hhh", -1), "invalid input")
        self.assertEqual(sum("hhh", "hhh"), "invalid input")
        self.assertEqual(sum(-1, "hhh"), "invalid input")

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(-1, -1), 1)
        self.assertEqual(divide("hhh", -1), "invalid input")
        self.assertEqual(divide("hhh","hhh"), "invalid input")
        self.assertEqual(divide(-1, "hhh"), "invalid input")
        self.assertEqual(divide(9, 0), "invalid division")

    def test_sumArray(self):
        self.assertEqual(sumArray([10, 5]), 15)
        self.assertEqual(sumArray([-1, 1]), 0)
        self.assertEqual(sumArray([-1, -1]), -2)
        self.assertEqual(sumArray(["hhh", -1]), "invalid input")
        self.assertEqual(sumArray(["hhh","hhh"]), "invalid input")
        self.assertEqual(sumArray([-1, "hhh"]), "invalid input")

    def test_evenArray(self):
        self.assertEqual(evenArray([0, 5]), [])
        self.assertEqual(evenArray([-1, 1,2,4]), [2,4])
        self.assertEqual(evenArray([-1, -1,-2,-99]), [-2])
        self.assertEqual(evenArray(["hhh", -2]), "invalid input")

if __name__ == '__main__':
    unittest.main()

