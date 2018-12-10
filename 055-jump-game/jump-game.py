# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Determine if you are able to reach the last index.
#
# Example 1:
#
#
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
#
# Example 2:
#
#
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
#              jump length is 0, which makes it impossible to reach the last index.
#
#


'''
艹泥马有1w个1做测试啊。。。
改用备忘录法吧 递归伤不起
'''
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        end = len(nums) - 1
        if end<= 0:
            return True
        pos = end - 1
        while(True):
            while(nums[pos]<end - pos and pos>=0):   #只要小于等于就能跳到
                pos -= 1
            if pos == 0:
                return True
            if pos < 0:
                return False
            if pos>0:
                end = pos
                pos = end -1
                #return self.canJump(nums[:pos+1])  # nums[pos] 可以跳到

            
            
        
