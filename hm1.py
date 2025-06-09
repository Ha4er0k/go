import random
import timeit
import matplotlib.pyplot as plt
import heapq

def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result.extend(left[l:])
    result.extend(right[r:])
    return result

sizes = [100, 500, 1000, 2000]
results = {"Insertion Sort": [], "Merge Sort": [], "Timsort (sorted)": []}

for size in sizes:
    data = [random.randint(0, 10000) for _ in range(size)]

    time_insertion = timeit.timeit(lambda: insertion_sort(data), number=1)
    time_merge = timeit.timeit(lambda: merge_sort(data), number=1)
    time_timsort = timeit.timeit(lambda: sorted(data), number=1)

    results["Insertion Sort"].append(time_insertion)
    results["Merge Sort"].append(time_merge)
    results["Timsort (sorted)"].append(time_timsort)


plt.figure(figsize=(10, 6))
for label, timings in results.items():
    plt.plot(sizes, timings, marker="o", label=label)

plt.title("Порівняння часу виконання алгоритмів сортування")
plt.xlabel("Розмір масиву")
plt.ylabel("Час виконання (сек.)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


def merge_k_lists(lists):
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    result = []
    while heap:
        val, list_idx, element_idx = heapq.heappop(heap)
        result.append(val)
        if element_idx + 1 < len(lists[list_idx]):
            next_tuple = (lists[list_idx][element_idx + 1], list_idx, element_idx + 1)
            heapq.heappush(heap, next_tuple)
    return result


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
