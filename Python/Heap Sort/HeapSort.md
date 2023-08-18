# Heap Sort Algorithm in Python

The Heap Sort algorithm is a comparison-based sorting algorithm that utilizes a binary heap data structure to sort elements. It involves two main steps: building a heap and repeatedly extracting the maximum (for ascending order) element from the heap and placing it at the end of the sorted list.

## Step-by-Step Explanation

Let's go through the Heap Sort algorithm step-by-step using Python:

1. **Define the Heapify function**:

Heapify is a crucial step in the Heap Sort algorithm. It adjusts the position of an element in the heap to maintain the heap property.

```python
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
```

2. **Define the Heap Sort function**:

The Heap Sort function constructs the heap and repeatedly extracts the maximum element from it.

```python
def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
```

3. **Complete code**:

Putting all the parts together, the complete Python code for the Heap Sort algorithm is as follows:

```python
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

number_list = [5, 2, 9, 1, 5, 6]
heap_sort(number_list)
print("Sorted list:", number_list)
```

The output will be:

```
Sorted list: [1, 2, 5, 5, 6, 9]
```

Heap Sort has a time complexity of O(n log n), making it efficient for larger lists. It doesn't require additional memory like Merge Sort, but it involves complex index calculations.

## Algorithm Animation

Here's an animation illustrating how Heap Sort works:

![Heap Sort Animation](https://upload.wikimedia.org/wikipedia/commons/1/1b/Sorting_heapsort_anim.gif)
