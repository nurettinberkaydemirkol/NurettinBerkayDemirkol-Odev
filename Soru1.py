#gerekli kütüphanelerin eklenmesi
import time
import random

arr = [random.randint(0, 100000) for _ in range(10000)]

#brute force ile en büyük sayıyı bulmak için - O(n) ile çalışır
def find_max(arr):
    max_num = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
    return max_num

startTime = time.time()
max_num = find_max(arr)
stopTime = time.time()

print("max sayi: ", max_num)
print("Süre: ", stopTime - startTime, "saniye")

#quick sort ile bölerek en büyük elemanı ayırır - o(logn) ile çalışır
def find_max_quick(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    else:
        mid = len(arr) // 2
        left_max = find_max_quick(arr[:mid])
        right_max = find_max_quick(arr[mid:])
        return left_max if left_max > right_max else right_max

startTime_quick = time.time()
max_num_quick = find_max_quick(arr)
stopTime_quick = time.time()

print("max sayi: ", max_num_quick)
print("Süre: ", stopTime_quick - startTime_quick, "saniye")
