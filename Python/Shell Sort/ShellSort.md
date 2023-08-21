# Shell Sort Algorithm in Python

The Shell Sort algorithm is an efficient variation of the insertion sort algorithm that breaks down the list into smaller sublists and sorts them using insertion sort. The gap sequence determines how the sublists are formed and sorted.

## Step-by-Step Explanation

Let's go through the Shell Sort algorithm step-by-step using Python:

1. **Define the Shell Sort function**:

```python
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
```

2. **Sort sublists with insertion sort**:

Use insertion sort to sort sublists with a specified gap. The gap decreases in each iteration.

```python
        for i in range(gap, n):
            current = arr[i]
            j = i
            while j >= gap and arr[j - gap] > current:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = current
```

3. **Reduce the gap**:

After each pass of sorting with a specific gap, reduce the gap size.

```python
        gap //= 2
```

4. **Complete code**:

Putting all the parts together, the complete Python code for the Shell Sort algorithm is as follows:

```python
def shell_sort(arr):
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

number_list = [5, 2, 9, 1, 5, 6]
shell_sort(number_list)
print("Sorted list:", number_list)
```

The output will be:

```
Sorted list: [1, 2, 5, 5, 6, 9]
```

Shell Sort has a time complexity that depends on the gap sequence used. It generally performs better than insertion sort for larger lists. The choice of gap sequence affects the algorithm's efficiency.

## Algorithm Animation

Here's an animation illustrating how Shell Sort works:

![Shell Sort Animation](https://upload.wikimedia.org/wikipedia/commons/d/d8/Sorting_shellsort_anim.gif)
