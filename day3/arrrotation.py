# arr = [1, 2, 3, 4, 5]
# n = len(arr)
# k = 2  # Number of rotations

# # Rotate array to the left by k positions
# rotated = arr[k % n :] + arr[: k % n]
# print(rotated)




#p2
# arr=[1,2,3,4,5]
# n=len(arr)
# l1=[]
# k = 2
# # Initialize l1 with n elements first
# l1 = [0] * n
# for i in range(n):
#     l1[(i+k)%n] = arr[i]

# print(l1)
        
#2
arr = [1, 2, 3, 4, 5]
k = 2

# Right rotation by k
rotated = arr[-k:] + arr[:-k]

print(rotated)

#3
# k=2
# n=len(arr)
# def rotate(arr,k):
#     k=k%n
# rotate(arr,0,n-1)
# rotate(arr,0,k-1)
# rotate(arr,k,n-1)
#2

# def reverse(arr, start, end):
#     while start < end:
#         arr[start], arr[end] = arr[end], arr[start]  # Swap elements
#         start += 1
#         end -= 1

# def rotate(arr, k):
#     n = len(arr)
#     k = k % n  # Handle k > n
#     reverse(arr, 0, n-1)      # Step 1: Reverse whole array
#     reverse(arr, 0, k-1)      # Step 2: Reverse first k elements
#     reverse(arr, k, n-1)      # Step 3: Reverse rest
#     return arr

# # Example usage
# arr = [1, 2, 3, 4, 5]
# k = 2
# rotated = rotate(arr, k)
# print(rotated)

# :



