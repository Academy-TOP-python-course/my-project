# from multiprocessing import Process, shared_memory, Lock
# import array
#
# def worker(shm_name, lock):
#     shm = shared_memory.SharedMemory(name=shm_name)
#     counter = array.array('q', shm.buf)  # 'q' означает целые числа (int64)
#
#     for _ in range(5):
#         with lock:
#             counter[0] += 1  # Увеличиваем счётчик
#
#     shm.close()
#
# if __name__ == "__main__":
#     shm = shared_memory.SharedMemory(create=True, size=array.array('q', [0]).itemsize)  # Создаём разделяемую память для int64
#     counter = array.array('q', shm.buf)
#     counter[0] = 0  # Инициализируем счётчик значением 0
#
#     lock = Lock()
#     processes = [Process(target=worker, args=(shm.name, lock)) for _ in range(3)]
#
#     for p in processes:
#         p.start()
#     for p in processes:
#         p.join()
#
#     final_value = array.array('q', shm.buf)[0]
#     print("Итоговое значение:", final_value)
#
#     shm.close()
#     shm.unlink()

from multiprocessing import Process, shared_memory
import array
import time
import random
from datetime import datetime


def worker(shm_name, index):
    """Процесс-работник"""
    shm = shared_memory.SharedMemory(name=shm_name)

    # Разное время работы
    work_time = random.uniform(1, 5)
    time.sleep(work_time)

    # Читаем число
    data = array.array('i')
    data.frombytes(bytes(shm.buf[:20]))
    num = data[index]
    result = num * num

    # Записываем результат
    data[index] = result
    shm.buf[:20] = data.tobytes()

    print(f"Процесс {index}: {num} -> {result} (спал {work_time:.1f} сек)")

    shm.close()


def monitor(shm_name, total):
    """Монитор - читает память и показывает изменения"""
    shm = shared_memory.SharedMemory(name=shm_name)

    print("\nМОНИТОРИМ ИЗМЕНЕНИЯ:")
    last_state = None

    for _ in range(10):  # Проверим 10 раз
        # Читаем текущее состояние памяти
        current = array.array('i')
        current.frombytes(bytes(shm.buf[:20]))
        current_list = current.tolist()

        # Если изменилось - показываем
        if current_list != last_state:
            print(f"Текущий массив: {current_list}")
            last_state = current_list.copy()

        time.sleep(0.5)  # Проверяем каждые 0.5 секунды

    shm.close()


if __name__ == "__main__":
    # Данные
    data = array.array('i', [2, 3, 5, 7, 11])

    print(f"Исходные числа: {data.tolist()}")

    # Создаём память
    shm = shared_memory.SharedMemory(create=True, size=20)
    shm.buf[:20] = data.tobytes()

    # Запускаем workers
    workers = []
    for i in range(len(data)):
        p = Process(target=worker, args=(shm.name, i))
        workers.append(p)
        p.start()
        print(f"Запущен процесс {i}")

    # Запускаем монитор (читает память "на лету")
    monitor_process = Process(target=monitor, args=(shm.name, len(data)))
    monitor_process.start()

    # Ждём всех
    for p in workers:
        p.join()

    monitor_process.terminate()  # Останавливаем монитор
    monitor_process.join()

    # Финальный результат
    final = array.array('i')
    final.frombytes(bytes(shm.buf[:20]))

    print(f"ИТОГОВЫЙ МАССИВ: {final.tolist()}")

    # Очистка
    shm.close()
    shm.unlink()
    print("Память очищена")