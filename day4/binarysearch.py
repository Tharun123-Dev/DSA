#Binary search is a fast and efficient searching algorithm used to find the position of a target value within a sorted array or list.
#  It works by repeatedly dividing the search interval in half until the target value is found or the interval becomes empty.
#  In this video, Varun sir will explain binary search in detail with relevant examples.
def binary(array,target):
    left,right=0,len(array)-1
    while left<=right:
        mid=(left+right)//2
        if array[mid]==target:
            return [mid]
        elif array[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return-1
print(binary([10,20,30,40,50,70],30))

#2 first occurance and last occurence of the code
def first_occurrence(array, target):
    left, right = 0, len(array) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            result = mid
            right = mid - 1  # move left to find first occurrence
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result


def last_occurrence(array, target):
    left, right = 0, len(array) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            result = mid
            left = mid + 1  # move right to find last occurrence
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result


# Example usage
arr = [10, 20, 20, 20, 20, 20, 40, 60]
target = 20

print("First Occurrence:", first_occurrence(arr, target))
print("Last Occurrence:", last_occurrence(arr, target))
