def bubbleSort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


arr = [5, 1, 90, 75, 33, 23, 65, 18, 33]
print(arr)
print(bubbleSort(arr))
