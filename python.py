import unittest

def add(num1, num2):
    if type(num1) == float and type(num2) == float:
        return num1 + num2
    else:
        return "Math Error"

def div(num1, num2):
    if type(num1) == float and type(num2) == float:
        if(num2 == 0): 
            return "Math Error"
        return num1//num2
    else:
        return "Invalid input"

def arr(arr):
    sum=0
    for num in arr:
        if type(num) == float:
            sum += num
        else:
            return "Math Error"
    return sum

def list(list):
    list = []
    for num in list:
        if type(num) == float and num % 2 == 0:
            list.append(int(num))
    return list



    class TestTasks(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(8, 10), 18)
        self.assertEqual(add(4, -7), -3)
        self.assertEqual(add(-6, -5), -11)
        self.assertEqual(add(74, 'p'), "Math Error")
        self.assertEqual(add('o', 88 ), "Math Error")

    def test_div(self):
        self.assertEqual(divide(20, 4), 5)
        self.assertEqual(divide(-9, 3), -3)
        self.assertEqual(divide(11, 4), 2)
        self.assertEqual(divide(7, 0), "Math Error")
        self.assertEqual(divide(3, 'k'), "Invalid input")
        self.assertEqual(divide('s', 7), "Invalid input")

    def test_arr(self):
        self.assertEqual(sum_arr([8, 5 , 9 , 3]), 25)
        self.assertEqual(sum_arr([1, -8 , 9 , 6  ,-7]), 0)
        self.assertEqual(sum_arr(['m' , 'a' , 'h' , 7]), "Math Error")

    def test_list(self):
        self.assertEqual(even_list([1, 2, 3, 4 , 6 , 7 , 8]), [2, 4, 6 ,8])
        self.assertEqual(even_list([3 , 6 , 9 , 12 , 15 , 18]), [6 , 12 , 18])
        self.assertEqual(even_list([1 , 3 , 5 , 7]), [])
        self.assertEqual(even_list(['m' , 'a' , 'h' , 7 , 8]), [8])
        self.assertEqual(even_list(['m' , 'a' , 'h']), [])

if __name__ == '__main__':
    unittest.main()