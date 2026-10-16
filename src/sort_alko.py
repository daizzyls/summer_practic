import random


def merge_sortt(arr):

    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2

    left = merge_sortt(arr[:middle])
    right = merge_sortt(arr[middle:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def selection_sort(arr):
    for i in range(0, len(arr)):
        min_ind = i
        j = i + 1
        while j < len(arr):
            if arr[j] < arr[min_ind]:
                min_ind = j
            j += 1

        if min_ind != i:
            arr[i], arr[min_ind] = arr[min_ind], arr[i]

    return arr


def insert_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

    return arr


def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    return arr


def heapify(arr, space, i):

    daddy = i
    left_kid = 2 * i + 1
    right_kid = 2 * i + 2

    if left_kid < space and arr[left_kid] > arr[daddy]:
        daddy = left_kid

    if right_kid < space and arr[right_kid] > arr[daddy]:
        daddy = right_kid

    if daddy != i:
        arr[i], arr[daddy] = arr[daddy], arr[i]

        heapify(arr, space, daddy)


def heap_sort(arr):
    space = len(arr)

    for i in range(space // 2 - 1, -1, -1):
        heapify(arr, space, i)

    for i in range(space - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[random.randint(0, len(arr) - 1)]  # Случайный опорный элемент
    left, middle, right = [], [], []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    return quick_sort(left) + middle + quick_sort(right)


def counting_sort_for_radix(arr: list[int], exp: int):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr: list[int]):
    if not arr:
        return arr

    max_val = max(arr)

    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

    return arr


def counting_sort(arr: list[int]) -> list[int]:
    if not arr:
        return arr

    min_val = min(arr)
    max_val = max(arr)
    range_of_elements = max_val - min_val + 1

    count = [0] * range_of_elements
    output = [0] * len(arr)

    for num in arr:
        count[num - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        current = arr[i]
        output[count[current - min_val] - 1] = current
        count[current - min_val] -= 1

    return output


def bucket_sort(arr: list[float]) -> list[float]:
    if not arr:
        return arr

    min_val = min(arr)
    max_val = max(arr)

    if min_val == max_val:
        return arr.copy()

    n = len(arr)
    buckets: list[list[float]] = [[] for _ in range(n)]

    for num in arr:
        bucket_index = int((num - min_val) / (max_val - min_val) * (n - 1))
        buckets[bucket_index].append(num)

    for bucket in buckets:
        bucket.sort()

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr
