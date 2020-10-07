# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if end < start:
        return -1
    # find middle
    middle = (start + end) // 2

    if target < arr[middle]:
        new_high = middle - 1
        return binary_search(arr, target, start, new_high)
    elif target > arr[middle]:
        new_low = middle + 1
        return binary_search(arr, target, new_low, end)
    else:
        return middle

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass