# Merge Sort Algorithm in Python

The Merge Sort algorithm is a popular sorting algorithm that follows the Divide and Conquer approach. It divides the input list into two halves, recursively sorts each half, and then merges the two sorted halves back together to obtain the final sorted list.

## Step-by-Step Explanation

Let's go through the Merge Sort algorithm step-by-step using Python:

1. Define the Merge Sort function:

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
```

2. Divide the list into two halves:

Find the middle index of the list and split it into two halves, left and right.

```python
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
```

3. Recursively sort each half:

Call the merge_sort function on both left and right halves to sort them.

```python
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
```

4. Merge the sorted halves:

Merge the two sorted halves back together to obtain the final sorted list.

```python
    return merge(left_half, right_half)
```

5. Define the merge function:

The merge function takes two sorted lists and merges them into a single sorted list.

```python
def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result
```

6. Result verification:

The final sorted list will be returned from the `merge_sort` function.

7. Complete code:

Putting all the parts together, the complete Python code for the Merge Sort algorithm is as follows:

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result

number_list = [5, 2, 9, 1, 5, 6]
sorted_list = merge_sort(number_list)

print("Sorted list:", sorted_list)
```

The output will be:

```
Sorted list: [1, 2, 5, 5, 6, 9]
```

Merge Sort has a time complexity of O(n log n) in the worst-case scenario, making it more efficient than Insertion Sort and Bubble Sort for larger lists.

## Algorithm Animation

![Merge Sort Animation](https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif)
