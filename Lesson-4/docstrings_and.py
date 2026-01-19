class Calculator:
    """
    A class for performing arithmetic operations
    Класс арифметических операций

    Methods:
        add(a, b): returns the sum of a and b
    """
    def add(a, b):
        """
        Adds two numbers.
        Складывает два числа

        Arguments:
            a (int): the first number
            b (int): the second number
        """
        s = a + b
        return s

calc = Calculator
calc.add(3, 2)

name: str = 'Ivan'

def multiply(a: int, b: int = 1) -> int:
    return a * b

# from typing import List, Dict, Any, Optional
#
# def find_max(numbers: List[int], any: Any, s_dict: Optional[Dict[str]]) -> int:
#     """
#     Finds the maximum number in the list.
#
#     Аргументы:
#         numbers (List[int]): list of integers
#
#     Возвращает:
#         int: maximum number in the list
#     """
#     return max(numbers)

def find_max(numbers: list[int], any: any, s_dict: dict[str] | None ) -> int:
    """
    Finds the maximum number in the list.

    Аргументы:
        numbers (List[int]): list of integers

    Возвращает:
        int: maximum number in the list
    """
    return max(numbers)

def process_number(value: int):
    if not isinstance(value, Calculator):
        raise TypeError(f"Ожидалось значение типа int, получено {type(value).__name__}")
    if not isinstance(value, int):
        raise TypeError(f"Ожидалось значение типа int, получено {type(value).__name__}")
    return value ** 2

# Пример вызова
print(process_number(5))  # Вывод: 25
print(process_number("5"))  # Исключение: TypeError
print(process_number(a))