"""
Задание 1. Анализ продаж

Ситуация: мы работаем в отделе аналитики и получаем CSV-файл с данными о продажах за месяц. Каждый ряд содержит следующую информацию: наименование товара, количество проданных единиц и цену за единицу.

Задача — необходимо вычислить общий доход для каждого товара и общий доход за месяц.

Реализуем функцию analyze_sales(file_path), которая:

Читает данные из CSV-файла.
Вычисляет общий доход для каждого товара (количество × цена).
Возвращает итоговый доход за месяц.
"""

import csv
from pathlib import Path


def analyze_sales(file_path):
    total_revenue = 0

    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            quantity = int(row['quantity'])
            price = float(row['price'])
            total_revenue += quantity * price

    return total_revenue

file_path = Path.cwd() / "prac.csv"
print("total_revenue: ", analyze_sales(file_path=file_path))
