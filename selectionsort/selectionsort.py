#selection sort
arr=[2,5,3,1,4,6,3,2]
n=len(arr)
for i in range (0,n-1):
    min=i
    for j in range (i+1,n):
        if arr[j]<arr[min]:
            min=j
    arr[i],arr[min]=arr[min],arr[i]
print(arr)

        
#  Definition:

# Insertion Sort is a simple sorting algorithm that builds the final sorted list one item at a time.
# It works like sorting playing cards in your hand — you pick one card at a time and place it in the correct position.

#  Algorithm Steps:

# Start from the second element (index 1).

# Compare the current element with the elements before it.

# Shift all larger elements one position to the right.

# Insert the current element in the correct position.

# Repeat until the array is sorted.

#  Example:

# Let’s sort this list:
# arr = [5, 3, 4, 1, 2]

# Step	Current Element	Process	Result
# 1	3	Compare with 5 → insert before	[3, 5, 4, 1, 2]
# 2	4	Compare with 5 → insert before	[3, 4, 5, 1, 2]
# 3	1	Move 5, 4, 3 → insert at start	[1, 3, 4, 5, 2]
# 4	2	Move 5, 4, 3 → insert after 1	[1, 2, 3, 4, 5]

#  Sorted list = [1, 2, 3, 4, 5]

#  Python Program:
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]       # Current element
        j = i - 1
        # Move elements greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example
arr = [5, 3, 4, 1, 2]
insertion_sort(arr)
print("Sorted array:", arr)