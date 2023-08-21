def shellSort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            current = arr[i]
            j = i
            while j >= gap and arr[j - gap] > current:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = current
        gap //= 2
    return arr


arr = [77, 34, 95, 110, 1, 0, 55, 69, 99]
print(arr)
print(shellSort(arr))
