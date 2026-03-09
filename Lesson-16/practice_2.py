from multiprocessing import Process, Queue

def power_numbers(numbers, exponent, result_queue):
    results = [num ** exponent for num in numbers]
    result_queue.put(results)

if __name__ == "__main__":
    numbers = list(range(1, 21))
    exponent = 2
    num_processes = 4

    result_queue = Queue()

    chunk_size = len(numbers) // num_processes
    processes = []
    for i in range(num_processes):
        start_idx = i * chunk_size
        end_idx = (i + 1) * chunk_size if i < num_processes - 1 else len(numbers)
        chunk = numbers[start_idx:end_idx]

        process = Process(target=power_numbers, args=(chunk, exponent, result_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    all_results = []
    while not result_queue.empty():
        all_results.extend(result_queue.get())

    print("Результаты:", all_results)
