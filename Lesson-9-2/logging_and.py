# # import logging
# #
# # # Настройка базового конфигуратора
# # logging.basicConfig(level=logging.DEBUG)
# #
# #
# # logging.debug('Это сообщение отладочного уровня')
# # logging.info('Это информационное сообщение')
# # logging.warning('Это предупреждение')
# # logging.error('Это сообщение об ошибке')
# # logging.critical('Это критическая ошибка')
#
# import logging
#
# # Настройка логгера
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s - %(levelname)s - %(filename)s : %(lineno)d - %(message)s'
# )
#
# logging.debug('Это отладочное сообщение')
# logging.info('Это информационное сообщение')
# logging.warning('Это предупреждающее сообщение')
# logging.error('Это ошибка')

# import logging
#
# # Создание логгера
# logger = logging.getLogger('example_logger')
# logger.setLevel(logging.DEBUG)
#
# # Создание обработчика для вывода в консоль
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.INFO)
#
# # Форматирование сообщений
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# console_handler.setFormatter(formatter)
#
# # Добавление обработчика к логгеру
# logger.addHandler(console_handler)
#
# # Логирование
# logger.debug('Это сообщение DEBUG')
# logger.info('Это сообщение INFO')
# logger.warning('Это сообщение WARNING')

# import logging
#
# # Создание логгера
# logger = logging.getLogger('example_logger')
# logger.setLevel(logging.DEBUG)
#
# # Создание обработчика для записи в файл
# file_handler = logging.FileHandler('error.log')
# file_handler.setLevel(logging.ERROR)
# file_handler_all = logging.FileHandler('all.log')
# file_handler_all.setLevel(logging.INFO)
#
# # Форматирование сообщений
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)
# file_handler_all.setFormatter(formatter)
#
# # Добавление обработчика к логгеру
# logger.addHandler(file_handler)
# logger.addHandler(file_handler_all)
#
# # Логирование
# logger.debug('Это отладочное сообщение')
# logger.info('Это информационное сообщение')
# logger.warning('Это предупреждающее сообщение')
# logger.error('Это ошибка')

# import logging
#
# # Настройка логгера
# logging.basicConfig(level=logging.ERROR)
#
# user = "Петя"
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     logging.exception('Произошла ошибка при делении на ноль. Вызвно: %s', user)

# from datetime import datetime
#
# # Текущая дата и время
# now = datetime.now()
# print(now)  # Например, 2025-01-08 14:30:45.123456
#
# # Создание объекта datetime с конкретными значениями
# custom_datetime = datetime(2023, 5, 15, 14, 30, 45)
# print(custom_datetime)  # 2023-05-15 14:30:45

# from datetime import datetime, timedelta
#
# # Разница в 5 дней
# delta = timedelta(days=5)
# print(delta)  # 5 days, 0:00:00
#
# # Арифметика с датами
# today = datetime.today()
# future_date = today + timedelta(days=10)
# print(future_date)  # Текущая дата + 10 дней

from datetime import datetime

now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
print(formatted_date)  # 2025-01-08 14:30:45