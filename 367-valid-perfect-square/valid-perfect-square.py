# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
# Note: Do not use any built-in library function such as sqrt.
#
# Example 1:
#
#
#
# Input: 16
# Output: true
#
#
#
# Example 2:
#
#
# Input: 14
# Output: false
#
#
#


class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        l = 0
        h = num
        while(l<h):
            mid = (l + h)//2 
            #print(mid)
            if mid**2 == num:
                return True
            elif mid ** 2 > num:
                h = mid
            elif mid **2 < num:
                l = mid
            if h-l == 1:  #俩数差为1
                return False
            #print(l,h,h-l)
        return False
                
        
