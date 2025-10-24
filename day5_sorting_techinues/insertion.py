#bubble sort---to asc
#check consecutive numbers and solve the swap
#1 4 5 7 3           1 4 5 3 7        1 4 3 5 7    134 57
#1  4 5 7 3          1  4 5 3 7       1 3 4 5 7    13457
#1 4 5 7 3           1 4 5 3 7
#1 4 5 3 7           1 4 3 5 7

#bubble sort--comparing consecutive numbers
arr = [1, 4, 5, 7, 2]
n = len(arr)

for i in range(n-1):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:  
            arr[j], arr[j+1] = arr[j+1], arr[j] 

print(arr)


#insertion sort--inserting element at the right or correct position
#---divided into two parts----left part always sorted---right part is unsorted
#---right to side elements fixed to left side sorted 
#example:74351
#7 4 3 5 1
#4 7 3 5 1
#3 4 7 5 1
#3 4 5 7 1
#1 3 4 5 7

arr=[7,4,3,5,1]
n=len(arr)
for i in range (1,n):
    key=arr[i]
    for j in range (i-1,-1,-1):
        if arr[j]>key:
            arr[j+1]=arr[j]
        else:
            arr[j+1]=key
            break
    else:
        arr[0]=key
print(arr)

