"""
Ситуация: мы работаем в IT-компании, и нам нужно обработать данные с задачами сотрудников. Данные хранятся в JSON-файле, где каждая задача содержит название, исполнителя и статус (выполнено или нет).

Задача — необходимо сформировать отчёт, в котором указано, сколько задач выполнил каждый сотрудник.

Реализуем функцию generate_report(json_file_path), которая:

Читает данные из JSON-файла.
Подсчитывает количество выполненных задач для каждого сотрудника.
Возвращает отчёт в виде словаря.
"""

import json
from collections import defaultdict
from pathlib import Path


def generate_report(json_file_path):
    report = defaultdict(int)

    with open(json_file_path, mode='r') as file:
        tasks = json.load(file)
        for task in tasks:
            if task['status'] == 'completed':
                report[task['assignee']] += 1

    return dict(report)

json_file_path = Path.cwd() / "prac_2.json"
print("report: ", generate_report(json_file_path=json_file_path))