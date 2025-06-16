def binary_search_with_upper_bound(arr, target):
# Виконує двійковий пошук у відсортованому списку дробових чисел.
#Повертає кортеж:
#кількість ітерацій, потрібних для пошуку
#найменше число, яке є більшим або рівним за target (верхня межа)
    
    left = 0
    right = len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        mid_val = arr[mid]

        if mid_val < target:
            left = mid + 1
        else:
            upper_bound = mid_val
            right = mid - 1

    return iterations, upper_bound



if __name__ == "__main__":
#Відсортований список дробових чисел
    arr = [0.1, 0.5, 1.0, 1.5, 2.2, 3.7, 4.4, 5.0]
    
    target = 3.0
    
    iters, upper = binary_search_with_upper_bound(arr, target)
    print(f"Кількість ітерацій: {iters}")
    print(f"Верхня межа для {target}: {upper}")
