def insertionSort(array):
    n = len(array)
    for i in range(1, n):
        actual = array[i]
        j = i - 1
        while j >= 0 and actual < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = actual
    return array


arr = [88, 4, 46, 69, 10, 1, 0, 55]
print(arr)
print(insertionSort(arr))
