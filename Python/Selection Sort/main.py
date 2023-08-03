def selectionSort(array):
    n = len(array)
    for i in range(n - 1):
         min_index = i
         for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
         array[i], array[min_index] = array[min_index], array[i]
    return array


arr = [77, 34, 95, 110, 1, 0, 55, 69, 99]
print(arr)
print(selectionSort(arr))