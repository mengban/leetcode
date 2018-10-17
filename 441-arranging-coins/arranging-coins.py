# You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
#
# Given n, find the total number of full staircase rows that can be formed.
#
# n is a non-negative integer and fits within the range of a 32-bit signed integer.
#
# Example 1:
#
# n = 5
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
#
# Because the 3rd row is incomplete, we return 2.
#
#
#
# Example 2:
#
# n = 8
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
#
# Because the 4th row is incomplete, we return 3.
#
#


class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==0:
            return 0
        end = 65536
        start = 1     
        flag = True
        while(flag):
            mid = (start+end)//2
            if mid*(mid+1)/2 > n:
                end = mid
            else:
                start = mid
            if (mid*(mid+1)/2) <= n and ((mid+1)*(mid+2)/2) > n:
                flag = False
        return mid
            
                
        
