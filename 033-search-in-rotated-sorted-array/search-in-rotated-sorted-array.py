# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Example 1:
#
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
#
#
# Example 2:
#
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
#


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1

        while(r>=l):
            mid = (r+l)//2
            if nums[mid] == target : # mid 刚好是target
                return mid

            if nums[l] <= nums[mid]: # 情况1  why nums[l] < nums[mid] don't pass [3 1] 1 对2求整 mid最有可能等于l 
                if nums[l]<=target<=nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:# 情况二
                if nums[mid]<=target<=nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
        
