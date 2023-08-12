# Quick Sort Algorithm in Python

The Quick Sort algorithm is another efficient sorting algorithm that follows the Divide and Conquer approach. It selects a pivot element from the list and partitions the list into two sublists: elements less than the pivot and elements greater than the pivot. This process is repeated recursively on the sublists until the entire list is sorted.

## Step-by-Step Explanation

Let's go through the Quick Sort algorithm step-by-step using Python:

1. Define the Quick Sort function:

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
```

2. Choose a pivot element:

Select a pivot element from the list. This can be done using various methods, such as selecting the first element, the last element, or a random element. For this example, let's choose the last element as the pivot.

```python
    pivot = arr[-1]
    left = []
    right = []
```

3. Partition the list:

Partition the list into two sublists: elements less than the pivot and elements greater than the pivot.

```python
    for element in arr[:-1]:
        if element < pivot:
            left.append(element)
        else:
            right.append(element)
```

4. Recursively sort sublists:

Recursively call the quick_sort function on the left and right sublists.

```python
    left = quick_sort(left)
    right = quick_sort(right)
```

5. Combine sublists and pivot:

Combine the sorted left sublist, pivot, and sorted right sublist to obtain the final sorted list.

```python
    return left + [pivot] + right
```

6. Result verification:

The final sorted list will be returned from the `quick_sort` function.

7. Complete code:

Putting all the parts together, the complete Python code for the Quick Sort algorithm is as follows:

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = []
    right = []

    for element in arr[:-1]:
        if element < pivot:
            left.append(element)
        else:
            right.append(element)

    left = quick_sort(left)
    right = quick_sort(right)

    return left + [pivot] + right

number_list = [5, 2, 9, 1, 5, 6]
sorted_list = quick_sort(number_list)

print("Sorted list:", sorted_list)
```

The output will be:

```
Sorted list: [1, 2, 5, 5, 6, 9]
```

Quick Sort has an average time complexity of O(n log n), making it highly efficient for most cases. However, its worst-case time complexity is O(n^2), which can be mitigated using various techniques like selecting a good pivot or using randomized Quick Sort.

## Algorithm Animation

![Quick Sort Animation](https://upload.wikimedia.org/wikipedia/commons/6/6a/Sorting_quicksort_anim.gif)
