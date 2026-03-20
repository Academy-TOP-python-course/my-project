# import multiprocessing
#
# def increment(shared_value):
#     for _ in range(10):
#         shared_value.value += 1
#
# if __name__ == '__main__':
#     shared_value = multiprocessing.Value('i', 0)
#     process = multiprocessing.Process(target=increment, args=(shared_value,))
#     process.start()
#     process.join()
#
#     print(f"Итоговое значение: {shared_value.value}")

from multiprocessing import Process, Array
def square_elements(shared_array):
    for i in range(len(shared_array)):
        shared_array[i] = shared_array[i] ** 2
if __name__ == "__main__":
    shared_array = Array('i', [1, 2, 3, 4])
    process = Process(target=square_elements, args=(shared_array,))
    process.start()
    process.join()
    print("Итоговый массив:", list(shared_array))