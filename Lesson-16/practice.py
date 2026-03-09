import os
from multiprocessing import Pool
import math

def compute_factorial(n):
    return math.factorial(n)

if __name__ == "__main__":
    numbers = [5, 7, 10, 12, 15]
    print("process_count", os.cpu_count())
    with Pool(4) as pool:
        results = pool.map(compute_factorial, numbers)

    for n, result in zip(numbers, results):
        print(f"Факториал {n}: {result}")