# def binary(array,target):
#     left,right=0,len(array)-1
#     while left<=right:
#         mid=(left+right)//2
#         if array[mid]==target:
#             return [mid]
#         elif array[mid]==target:
#             left=mid+1
#         else:
#             right=mid-1
#     return-1
# print(binary([1,2,3,4,3,1],4))


def peak(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left +( right-left)) // 2

        
        if arr[mid] < arr[mid + 1]:
            left = mid + 1   
        else:
            right = mid      

        
    return left
print( peak([1,2,3,4,3]))


