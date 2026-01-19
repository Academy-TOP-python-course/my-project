"""
Задание 2. Площади фигур
Ситуация: представим, что мы работаем в архитектурном бюро, которому нужно автоматизировать расчёт площадей различных геометрических фигур. Начнём с квадрата, так как большинство участков земли имеют такую форму.
Задача — написать класс Square, который при инициализации принимает длину стороны (тип float), а также содержит метод area, возвращающий площадь квадрата. Не забудем использовать аннотацию типов в обоих методах и написать docstrings как для класса, так и для каждого метода.
Шаги реализации
Объявим класс Square и напишем для него docstrings. Укажем в нём:
для чего класс был создан;
основные методы.
Напишем метод __init__, который будет принимать длину стороны квадрата. В аннотации укажем, что она должна иметь тип float.
Напишем docstrings для метода __init__, где укажем описание и принимаемые параметры.
Объявим атрибут width класса Square.
Создадим метод get_area, который ничего не принимает, так как использует атрибут width для расчёта площади и возвращает число типа float.
Укажем для него docstrings, которые будут содержать:
описание метода;
принимаемые параметры;
возвращаемое значение.
"""

class Square:
    """
    A class to represent a square.

    Attributes:
        width (float): The width of the square.

    Methods:
        __init__(width): Initializes the width of the square
        get_area(): Returns the area of the square
    """

    def __init__(self, width: float):
        """
        Initializes the square with the given width.

        Parameters:
            width (float): The width of the square
        """
        self.width = width

    def get_area(self) -> float:
        """
        Calculates the area of the square

        Returns:
            float: The area of the square
        """
        return self.width ** 2