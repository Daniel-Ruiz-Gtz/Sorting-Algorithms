# Selection Sort Algorithm in Python

The Selection Sort algorithm is a simple sorting algorithm that divides the list into two parts: a sorted part and an unsorted part. In each iteration, it searches for the smallest element in the unsorted part and places it at the beginning of the sorted part. This process is repeated until the entire list is sorted.

## Step-by-Step Explanation

Let's go through the Selection Sort algorithm step-by-step using Python:

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

3. Find the index of the smallest element in the unsorted part:

In each iteration, we assume that the smallest element is the first one in the unsorted part. Then, we traverse the rest of the unsorted part to find the index of the smallest element in the list.

```python
    min_index = i
    for j in range(i + 1, n):
        if number_list[j] < number_list[min_index]:
            min_index = j
```

4. Swap the smallest element with the first element of the unsorted part:

Once we have found the index of the smallest element, we swap it with the first element of the unsorted part.

```python
    number_list[i], number_list[min_index] = number_list[min_index], number_list[i]
```

5. Result verification:

Once the outer loop has finished, the list will be completely sorted.

6. Complete code:

Putting all the parts together, the complete Python code for the Selection Sort algorithm is as follows:

```python
number_list = [5, 2, 9, 1, 5, 6]
n = len(number_list)

for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if number_list[j] < number_list[min_index]:
            min_index = j
    number_list[i], number_list[min_index] = number_list[min_index], number_list[i]

print("Sorted list:", number_list)
```

The output will be:

```
Sorted list: [1, 2, 5, 5, 6, 9]
```

Selection Sort has an average time complexity of O(n^2) in the worst-case scenario, making it less efficient than other sorting algorithms such as Merge Sort or Quick Sort. However, it can be useful for small lists or when memory space is limited since it only requires swapping elements instead of dividing the list into subsets.

## Algorithm Animation

![Selection Sort Animation](https://upload.wikimedia.org/wikipedia/commons/9/94/Selection-Sort-Animation.gif)
