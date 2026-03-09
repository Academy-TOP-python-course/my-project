# from multiprocessing import Process
#
# def say_hello():
#     print("Привет от процесса!")
#
# if __name__ == "__main__":
#     # Создаём процесс
#     process = Process(target=say_hello)  # Передаём функцию say_hello в процесс
#     process.start()  # Запускаем процесс
#     process.join()   # Ожидаем завершения процесса
import os
# from multiprocessing import Process
# import time
#
# def long_task():
#     print("Процесс начал работу.")
#     time.sleep(5)  # Имитируем длительную задачу
#     print("Процесс завершил работу.")
#
# if __name__ == "__main__":
#     process = Process(target=long_task)
#     process.start()
#
#     # Проверяем, работает ли процесс
#     time.sleep(2)
#     if process.is_alive():
#         print("Процесс все еще работает. Прерываем его.")
#         process.terminate()  # Принудительно завершаем процесс
#
#     process.join()  # Дожидаемся завершения процесса
#     print("Процесс завершён.")

# from multiprocessing import Process, Queue
# import time
#
# def producer(queue):
#     for i in range(5):
#         print(f"Производитель отправляет: {i}")
#         queue.put(i)  # Помещаем данные в очередь
#         time.sleep(1)
#
# def consumer(queue):
#     while True:
#         item = queue.get()  # Получаем данные из очереди
#         if item == "DONE":
#             break
#         print(f"Потребитель получил: {item}")
#
# if __name__ == "__main__":
#     queue = Queue()  # Создаём очередь
#
#     # Запускаем два процесса: производитель и потребитель
#     producer_process = Process(target=producer, args=(queue,))
#     consumer_process = Process(target=consumer, args=(queue,))
#
#     producer_process.start()
#     consumer_process.start()
#
#     # Ожидаем завершения процессов
#     producer_process.join()
#     # Отправляем сигнал завершения для потребителя
#     queue.put("DONE")
#     consumer_process.join()
#
#     print("Обмен данными завершен.")

# from multiprocessing import Process, Pipe
# import time
#
# def sender(conn):
#     for i in range(5):
#         print(f"Отправитель отправляет: {i}")
#         conn.send(i)  # Отправляем данные через канал
#         time.sleep(1)
#
# def receiver(conn):
#     while True:
#         data = conn.recv()  # Получаем данные из канала
#         if data == "DONE":
#             break
#         print(f"Получатель получил: {data}")
#
# if __name__ == "__main__":
#     # Создаём канал связи
#     parent_conn, child_conn = Pipe()
#
#     # Запускаем два процесса: отправитель и получатель
#     sender_process = Process(target=sender, args=(parent_conn,))
#     receiver_process = Process(target=receiver, args=(child_conn,))
#
#     sender_process.start()
#     receiver_process.start()
#
#     sender_process.join()
#     # Отправляем сигнал завершения для получателя
#     parent_conn.send("DONE")
#     receiver_process.join()
#
#     print("Обмен данными завершён.")

# from multiprocessing import Process, Queue
# import time
#
# # Функция, которая вычисляет квадрат числа и отправляет результат в очередь
# def compute_square(num, queue):
#     result = num ** 2
#     print(f"Процесс {num}: вычисление квадрата {num} = {result}")
#     queue.put(result)  # Отправляем результат в очередь
#     time.sleep(1)
#
# if __name__ == "__main__":
#     # Создаём очередь для обмена данными
#     queue = Queue()
#
#     # Создаём 3 процесса, каждый будет вычислять квадрат числа от 1 до 3
#     processes = []
#     for i in range(1, 4):
#         process = Process(target=compute_square, args=(i, queue))
#         processes.append(process)
#         process.start()
#
#     # Ожидаем завершения всех процессов
#     for process in processes:
#         process.join()
#
#     # Главный процесс забирает и выводит результаты из очереди
#     print("\nРезультаты вычислений:")
#     while not queue.empty():
#         result = queue.get()  # Получаем результат из очереди
#         print(f"Результат: {result}")
#
#     print("Все процессы завершены.")

# from multiprocessing import Pool
#
# def square(x):
#     return x ** 2
#
# if __name__ == "__main__":
#     # Создаём пул из 4 процессов
#     with Pool(processes=os.cpu_count()-2) as pool:
#         # Список чисел для обработки
#         numbers = [1, 2, 3, 4, 5, 6, 7, 8]
#
#         # Применяем функцию ко всем элементам с помощью map
#         results = pool.map(square, numbers)
#
#     print(f"Квадраты чисел: {results}")

from multiprocessing import Process, Queue
import time

# Функция, которая вычисляет квадрат числа и отправляет результат в очередь
def compute_square(num, queue):
    result = num ** 2
    print(f"Процесс {num}: вычисление квадрата {num} = {result}")
    queue.put(result)  # Отправляем результат в очередь
    time.sleep(1)

def run():
    # Создаём очередь для обмена данными
    queue = Queue()

    # Создаём 3 процесса, каждый будет вычислять квадрат числа от 1 до 3
    processes = []
    for i in range(1, 4):
        process = Process(target=compute_square, args=(i, queue))
        processes.append(process)
        process.start()

    # Ожидаем завершения всех процессов
    for process in processes:
        process.join()

    # Главный процесс забирает и выводит результаты из очереди
    print("\nРезультаты вычислений:")
    while not queue.empty():
        result = queue.get()  # Получаем результат из очереди
        print(f"Результат: {result}")

    print("Все процессы завершены.")

if __name__ == "__main__":
    run()