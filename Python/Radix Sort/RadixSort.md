# Radix Sort Algorithm in Python

Radix Sort is a non-comparative sorting algorithm that works by sorting numbers digit by digit. It takes advantage of the fact that numbers with more digits are larger. It sorts the numbers by considering the least significant digit first and then moving to the more significant digits.

## Step-by-Step Explanation

Let's go through the Radix Sort algorithm step-by-step using Python:

1. **Define the Radix Sort function**:

```python
def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
```

2. **Define the Counting Sort function for a specific digit**:

Counting Sort is used to sort the array based on a specific digit position.

```python
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]
```

3. **Complete code**:

Putting all the parts together, the complete Python code for the Radix Sort algorithm is as follows:

```python
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

number_list = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(number_list)
print("Sorted list:", number_list)
```

The output will be:

```
Sorted list: [2, 24, 45, 66, 75, 90, 170, 802]
```

Radix Sort has a time complexity of O(nk), where n is the number of elements and k is the number of digits in the maximum number. It is particularly efficient for sorting large integers or strings.

## Algorithm Animation

Here's an animation illustrating how Radix Sort works:

![Radix Sort Animation](https://miro.medium.com/v2/resize:fit:640/0*8LrHUNrYdJU16l-K)
