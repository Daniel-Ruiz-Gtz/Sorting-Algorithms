# Bubble Sort Algorithm in Python

The Bubble Sort algorithm is a simple sorting algorithm that compares adjacent elements in a list and swaps them if they are in the wrong order. This process is repeated several times until the entire list is sorted. It is named Bubble Sort because larger elements "bubble" to the end of the list during iterations.

## Step-by-Step Explanation

Let's go through the Bubble Sort algorithm step-by-step using Python:

1. Define the list of numbers:

```python
number_list = [5, 2, 9, 1, 5, 6]
```

2. Set up the outer loop:

The outer loop controls the number of passes required to ensure that the list is completely sorted. The number of passes needed is equal to the number of elements in the list minus one.

```python
n = len(number_list)
for i in range(n - 1):
```

3. Set up the inner loop:

The inner loop is responsible for comparing and possibly swapping adjacent elements in the list.

```python
    for j in range(n - i - 1):
```

4. Compare and perform swaps:

We compare the current element with the next one. If the current element is greater than the next one, we swap them so that the larger element "bubbles" to the end of the list.

```python
        if number_list[j] > number_list[j + 1]:
            number_list[j], number_list[j + 1] = number_list[j + 1], number_list[j]
```

5. Result verification:

Once both loops have finished, the list will be sorted in ascending order.

6. Complete code:

Putting all the parts together, the complete Python code for the Bubble Sort algorithm is as follows:

```python
number_list = [5, 2, 9, 1, 5, 6]
n = len(number_list)

for i in range(n - 1):
    for j in range(n - i - 1):
        if number_list[j] > number_list[j + 1]:
            number_list[j], number_list[j + 1] = number_list[j + 1], number_list[j]

print("Sorted list:", number_list)
```

The output will be:

```
Sorted list: [1, 2, 5, 5, 6, 9]
```

Bubble Sort is not efficient for large lists, as it has an average time complexity of O(n^2). However, it is useful for small or nearly sorted lists due to its simplicity.

## Algorithm Animation

![Bubble Sort Animation](https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif)
