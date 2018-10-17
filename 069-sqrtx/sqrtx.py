# Implement int sqrt(int x).
#
# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
#
# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
#
# Example 1:
#
#
# Input: 4
# Output: 2
#
#
# Example 2:
#
#
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
#              the decimal part is truncated, 2 is returned.
#
#


import math
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==1:
            return 1
        mid = x/2 
        l = 0
        r = x
        while(abs(mid**2 - x)>0.01):
            if mid**2 > x:
                r = mid
            else:
                l = mid
            mid = (r+l)/2
        return int(mid)
        #return int(math.sqrt(x))
