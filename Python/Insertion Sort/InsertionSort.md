# Insertion Sort Algorithm in Python

The Insertion Sort algorithm is a simple sorting algorithm that divides the list into two parts: a sorted part and an unsorted part. In each iteration, it takes an element from the unsorted part and inserts it into the correct position within the sorted part by shifting larger elements to the right. This process is repeated until all elements are in their sorted position.

## Step-by-Step Explanation

Let's go through the Insertion Sort algorithm step-by-step using Python:

1. Define the list of numbers:

```python
number_list = [5, 2, 9, 1, 5, 6]
```

2. Set up the outer loop:

The outer loop will iterate over each element of the list from the second element to the last one.

```python
n = len(number_list)
for i in range(1, n):
```

3. Save the current value and set an index for comparison:

In each iteration, we save the current value in a temporary variable and also set an index `j` for comparison with previous elements.

```python
    current = number_list[i]
    j = i - 1
```

4. Shift larger elements to the right:

We compare the current value with previous elements in the sorted part of the list. While the current value is less than the element at index `j`, we shift the element to the right to make space for the current value.

```python
    while j >= 0 and current < number_list[j]:
        number_list[j + 1] = number_list[j]
        j -= 1
```

5. Insert the current value in its correct position:

Once we have found the correct position for the current value in the sorted part, we insert it at that position.

```python
    number_list[j + 1] = current
```

6. Result verification:

Once the outer loop has finished, the list will be completely sorted.

7. Complete code:

Putting all the parts together, the complete Python code for the Insertion Sort algorithm is as follows:

```python
number_list = [5, 2, 9, 1, 5, 6]
n = len(number_list)

for i in range(1, n):
    current = number_list[i]
    j = i - 1
    while j >= 0 and current < number_list[j]:
        number_list[j + 1] = number_list[j]
        j -= 1
    number_list[j + 1] = current

print("Sorted list:", number_list)
```

The output will be:

```
Sorted list: [1, 2, 5, 5, 6, 9]
```

Insertion Sort has an average time complexity of O(n^2) in the worst-case scenario, but it is more efficient than Bubble Sort in most cases. It is especially useful for small or nearly sorted lists.

## Algorithm Animation

![Selection Insertion Animation](https://upload.wikimedia.org/wikipedia/commons/9/9c/Insertion-sort-example.gif)
