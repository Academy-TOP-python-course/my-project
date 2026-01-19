"""
Задание 2. Количество знаков препинания
Ситуация: коллега написал часть программы, которая работает с текстом. Задача функции,
которую нам передали, — вычислять количество знаков препинания в полученной строке.
Ниже представлена её реализация:

Задача — проверить, верно ли работает функция, и в случае найденных ошибок исправить их. Для поиска ошибок использовать pytest.
Шаги реализации
Напишем тесты, покрывающие все возможные ошибки.
В случае обнаружения ошибок исправим их. Каждое исправление поясним комментарием.
"""

import pytest

def count_punct_marks(string: str) -> int:
    total_count = 0
    for sym in ",.:;'!?":
        total_count += string.count(sym)
    return total_count


def test_empty_string():
   assert count_punct_marks("") == 0

def test_no_punctuation():
    assert count_punct_marks("Hello World") == 0

def test_single_punctuation():
    assert count_punct_marks("Hello World!") == 1

def test_multiple_punctuation():
    assert count_punct_marks("Hello, World! How are you?") == 3

def test_edge_case():
    assert count_punct_marks("!!!") == 3

def test_all_punctuation():
    assert count_punct_marks(".,:;!?") == 6
