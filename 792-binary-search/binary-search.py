# Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.
#
#
# Example 1:
#
#
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
#
#
#
# Example 2:
#
#
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
#
#
#  
#
# Note:
#
#
# 	You may assume that all elements in nums are unique.
# 	n will be in the range [1, 10000].
# 	The value of each element in nums will be in the range [-9999, 9999].
#
#


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ## 输入为1个数有bug
        # 输入不在一个区间里 23 24 行if-else 错误
        if not nums:
            return -1
        if nums[-1] < target or nums[0] > target: #最大值小于 target 直接返回
            return -1
        
        start = 0
        end = len(nums) - 1
        if end == 0:
            return 0 if nums[0]==target else -1
        while(end >=start):
            mid = (start + end)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target: # [mid] tar
                start = mid
            else:
                end = mid
            if (end -start ==1):
                if nums[start] == target:
                    return start
                if nums[end] == target:
                    return end
                else:
                    return -1
            
        
