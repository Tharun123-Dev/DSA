#math using also
# import math
# sqr=10
# a=math.sqrt(sqr)
# print(a)

# v=sqr**0.5
# print(v)

#binary search practice #leetcode 69
n=3
low=0
high=n
while((high-low)>0.0000000001):
    mid=((high+low)/2)
    if ((mid*mid)<n):
        low=mid
    else:
        high=mid
print(low)



class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        low, high = 1, x // 2
        while low <= high:
            mid = (low + high) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                low = mid + 1
            else:
                high = mid - 1

        return high  # integer part of sqrt(x)


