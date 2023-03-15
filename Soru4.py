#gerekli kütüphanelerin eklenmesi
import time
import random

arr = [random.randint(0, 100000) for _ in range(10000)]

#brute force ile sıralama
def brute_force_sirala(dizi):
    n = len(dizi)
    for i in range(n):
        for j in range(i+1, n):
            if dizi[j] < dizi[i]:
                dizi[i], dizi[j] = dizi[j], dizi[i]
    return dizi

startTime_brute = time.time()
sorted_arr_brute = brute_force_sirala(arr)
stopTime_brute = time.time()

print("siralanmış dizi: ", sorted_arr_brute)
print("Brute force ile süre: ", stopTime_brute - startTime_brute, "saniye")

#quick sort algoritması
def quick_sort(dizi):
    if len(dizi) <= 1:
        return dizi
    else:
        pivot = dizi[0]
        left = []
        right = []
        for i in range(1, len(dizi)):
            if dizi[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quick_sort(left) + [pivot] + quick_sort(right)

startTime_quick = time.time()
sorted_arr_quick = brute_force_sirala(arr)
stopTime_quick = time.time()

print("siralanmış dizi: ", sorted_arr_quick)
print("Quick sort ile süre: ", stopTime_quick - startTime_quick, "saniye")