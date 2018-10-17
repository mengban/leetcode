# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#
# Example 1:
#
#
# Input: [3,0,1]
# Output: 2
#
#
# Example 2:
#
#
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
#
#
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?


class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 1 if nums[0]==0 else 0
        nums.sort()
        if nums[0]!=0:        # 缺少最后一位或者第一位
            return 0
        if nums[len(nums)-1]!=len(nums):
            return len(nums)
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] == 2:
                return(int((nums[i+1]+nums[i])/2))  
        
