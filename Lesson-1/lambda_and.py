# def some_foo(a, b):
#     return a * b
#
# multiply = lambda a, b: a * b
# print("multiply: ", multiply(12, 3))
# # =================================
# arr = [1, 2, 3]
# print("arr: ", arr)
# newarr = list()
# for elem in arr:
#     newarr.append(elem**2)
# print("newarr: ", newarr)
#
# # map(func, []) -> итератор
# print("map: ", list(map(lambda x: x**2, arr)))
# =================================
arr = list(range(9))
print("arr: ", arr)
newarr = list()
for elem in arr:
    if elem % 2 == 0:
        newarr.append(elem)
print("newarr: ", newarr)

# filter(func, []) -> итератор
# выборка четных чисел из массива
print("filter: ", list(filter(lambda x: x % 2 == 0, arr)))
# =================================
from functools import reduce
arr = list(range(1, 6))
multiply = lambda a, b: a * b
print(reduce(multiply, arr)) # 120
# [1, 2, 3, 4, 5]
# a * b
# (1 * 2) = 2
#осталось [2, 3, 4, 5]
# 2 * 3 = 6
#осталось [6, 4, 5]
# 6 * 4 = 24
#осталось [24, 5]
# 24 * 5 = 120
# (((1 * 2) * 3) * 4) * 5 = 120
# =================================
# arr1 = [1, 2, 3]
# # arr2 = ["a", "b", "c", "d"]
# arr2 = ["a", "b"]
# print("zip: ", list(zip(arr1, arr2)))
# # [(1, 'a'), (2, 'b'), (3, 'c')]
# =================================
# arr = [1, 2, "hello", 4, "world"]
# print("arr: ", arr)
# arr = list(filter(lambda x: type(x) is str, arr))
# print("arr: ", arr)
# print("error", list(map(lambda x: len(x), arr)))

