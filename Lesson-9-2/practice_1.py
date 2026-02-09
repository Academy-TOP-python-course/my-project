import logging

# Создание логгера
logger = logging.getLogger('order_logger')
logger.setLevel(logging.INFO)

# Создание обработчика для записи в файл
file_handler = logging.FileHandler('order_errors.log')
file_handler.setLevel(logging.ERROR)

# Настройка формата логов
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)

# Пример логирования ошибки
try:
    # Симуляция ошибки при обработке заказа
    raise ValueError("Некорректные данные заказа")
except ValueError as e:
    logger.error(
        "Ошибка обработки заказа: %s",
        e,
        exc_info=True
    )