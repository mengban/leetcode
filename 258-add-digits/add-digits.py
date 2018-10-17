# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
#
# Example:
#
#
# Input: 38
# Output: 2 
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
#              Since 2 has only one digit, return it.
#
#
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?


class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # so easy
        s = str(num)
        while(len(s)>1):
            _sum = 0
            for item in s:
                _sum +=int(item)
            s = str(_sum)
        return int(s)
