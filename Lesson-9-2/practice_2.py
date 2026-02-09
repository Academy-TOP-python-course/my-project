from datetime import datetime, timedelta

# Функция для вычисления даты с учётом рабочих дней
def add_weekdays(start_date, num_days):
    current_date = start_date
    while num_days > 0:
        current_date += timedelta(days=1)
        if current_date.weekday() < 5:  # Понедельник - пятница
            num_days -= 1
    return current_date

# Получаем текущее время
date_now = datetime.now()

# Рассчитываем дату доставки (5 рабочих дней)
delivery_date = add_weekdays(date_now, 5)

# Выводим результат
print(f"Дата доставки: {delivery_date.strftime('%Y-%m-%d %H:%M:%S')}")