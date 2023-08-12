def quickSort(array):
    if len(array) <= 1:
        return array

    pivot = array[-1]
    left = []
    right = []

    for element in array[:-1]:
        if element < pivot:
            left.append(element)
        else:
            right.append(element)

    left = quickSort(left)
    right = quickSort(right)

    return left + [pivot] + right


arr = [77, 34, 95, 110, 1, 0, 55, 69, 99]
print(arr)
print(quickSort(arr))
