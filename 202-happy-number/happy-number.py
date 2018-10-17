# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
#
# Example: 
#
#
# Input: 19
# Output: true
# Explanation: 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
#


class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        _list = list(str(n))             
        _sum = 0
        _sumlist = []
        while True:
            l =len(_list)   # int 通过str 转为list 通过遍历求解  
            _sum = 0
            for i in range(l):
                _sum += int(_list[i])**2
                #_sum += pow(int(_list[i]),2)
            #print(_sum)
            if _sum == 1:
                #print('point!')
                return True
            else:
                _list = list(str(_sum))
                if _sum in _sumlist:
                    return False
                else:
                    _sumlist.append(_sum)
            #print(_sumlist) 
        
