def heapify(arr, n, i, compare_func):
    """Вспомогательная функция для создания кучи"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and compare_func(arr[left], arr[largest]) > 0:
        largest = left

    if right < n and compare_func(arr[right], arr[largest]) > 0:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, compare_func)


def heap_sort(arr, compare_func):
    """Пирамидальная сортировка"""
    if not arr:
        return arr

    n = len(arr)

    # Построение max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, compare_func)

    # Извлечение элементов из кучи
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, compare_func)

    return arr
