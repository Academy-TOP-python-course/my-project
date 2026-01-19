# def divide(a, b):
#     assert b != 0, "zero division"
#     return a / b
#
# divide(5, 2)    # 2.5
# divide(5, 0)    # AssertionError: zero division
#
# import unittest
#
# def divide(a, b):
#     if b == 0:
#         raise ValueError("Cannot divide by zero!")
#     return a / b
#
# class TestDivideFunction(unittest.TestCase):
#     def test_divide(self):
#         self.assertEqual(divide(10, 2), 5)
#         self.assertRaises(ValueError, divide, 10, 0)
#
# if __name__ == "__main__":
#     unittest.main()

add = lambda a, b: a + b

def test_add():
    assert add(2, 3) == 5  # Проверяем, что 2 + 3 = 5
    assert add(-1, 1) == 0  # Проверяем, что -1 + 1 = 0