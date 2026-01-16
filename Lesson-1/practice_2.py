"""
Задание 2. Список сотрудников

Ситуация: мы работаем в HR-отделе и собираем данные о сотрудниках. У нас есть три списка:

Имена сотрудников.
Их должности.
Зарплата.
Нам нужно объединить эти данные в одну строку формата «Имя-Должность-Зарплата» для каждого сотрудника.

Задача — реализовать функцию combine_employee_data(names, positions, salaries), которая принимает три списка одинаковой длины и возвращает список строк. Используем функцию zip для объединения данных и map для формирования строк.

Шаги реализации:

С помощью zip объединим три списка.
Используем map и лямбда-функцию для преобразования данных в нужный формат.
Вернём список строк.
"""

# def combine_employee_data(names, positions, salaries):
#     combined = zip(names, positions, salaries)
#     return list(map(lambda x: f"{x[0]} - {x[1]}: {x[2]}", combined))

def combine_employee_data(names, positions, salaries):
    combined = list(zip(names, positions, salaries))
    print("combined: ", combined)
    return some_foo(combined)

def some_foo(x):
    new_arr = []
    for i in x:
        new_arr.append(f"{i[0]} - {i[1]}: {i[2]}")
    return new_arr
#     # return list(map(lambda x: f"{x[0]} - {x[1]}: {x[2]}", combined))

names = ["Анна", "Борис", "Виктория", "Василий"]
positions = ["Менеджер", "Разработчик", "Аналитик", "Ген.дир"]
salaries = [80000, 120000, 90000]
print(combine_employee_data(names, positions, salaries))
# ['Анна - Менеджер: 80000', 'Борис - Разработчик: 120000', 'Виктория - Аналитик: 90000']