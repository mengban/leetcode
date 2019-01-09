# Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Example 1:
#
#
# Input: [2,2,3,2]
# Output: 3
#
#
# Example 2:
#
#
# Input: [0,1,0,1,0,1,99]
# Output: 99
#


'''
字典法
优化：分为3的倍数
pass


'''
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        table = [0 for i in range(32)]
        for item in nums:
            for i in range(32):
                table[31-i] += (item>>i)&1
        _bit = [x%3 for x in table] 
        print(_bit)
        ret = 0
        flag = False
        if _bit[0] == 1:
            flag = True
        if flag: #负数
            for j in range(32):
                if _bit[j] == 0:
                    _bit[j] = 1
                else:
                    _bit[j] = 0
        for i in range(32):
            if _bit[31-i] > 0:
                ret += _bit[31-i]*(2**i) 
        if flag:
            return -(ret+1)
        return ret
