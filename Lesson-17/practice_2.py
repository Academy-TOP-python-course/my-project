from multiprocessing import process, shared_memory, Lock
import array

def process_row(shm_name, row, cols, lock):
    shm = shared_memory.SharedMemory(name=shm_name)
    matrix = array.array('i', shm.buf)  # 'i' означает целые числа (int)
    start = row * cols  # начало строки
    end = start + cols  # конец строки

    with lock:
        for i in range(start, end):
            matrix[i] *= 2  # умножаем каждый элемент строки на 2

    shm.close()

if __name__ == "__main__":
    rows, cols = 3, 3
    data = [[i * cols + j for j in range(cols)] for i in range(rows)]  # создаём исходную матрицу
    flat_data = [item for sublist in data for item in sublist]  # преобразуем в одномерный список

    # создаём массив для хранения данных в разделяемой памяти
    arr = array.array('i', flat_data)
    shm = shared_memory.SharedMemory(create=True, size=arr.buffer_info()[1] * arr.itemsize)
    shm.buf[:] = arr.tobytes()  # копируем данные в разделяемую память

    lock = Lock()

    processes = [
        process(target=process_row, args=(shm.name, i, cols, lock))
        for i in range(rows)
    ]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    # читаем результат из разделяемой памяти
    result_matrix = array.array('i', shm.buf)
    result_matrix = [result_matrix[i * cols:(i + 1) * cols] for i in range(rows)]

    print("итоговая матрица:")
    for row in result_matrix:
        print(row)

    shm.close()
    shm.unlink()