# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
#
# Example 2:
#
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
#


'''update'''
'''
2019-2-26
采用二分查找法
降低时间复杂度
'''
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        l = len(nums)
        if l ==0:
            return [-1,-1]
        start = 0
        end = l-1
        while(nums[start] != target and start < l-1):
            start += 1
        while(nums[end] != target and end >=0):
            end -=1

        if start > end:
            return [-1,-1]
        return [start,end]
        '''

        l = 0
        r = len(nums) -1
        if r<0:
            return [-1,-1] 
        pos = -1
        start = 0
        end = 0
        while(r>=l):
            #print('while')
            mid = (l + r) // 2
            if nums[mid] == target:
                pos = mid
                break
            elif nums[mid] > target: ##   target mid
                r = mid - 1
            else:
                l = mid + 1
                
        if pos == -1:
            return [-1,-1]
        else:
            start = pos
            end = pos
            while start >=0 and nums[start] == target :
                start -= 1
            while end <=(len(nums)-1) and nums[end] == target:
                end += 1
        return [start+1,end-1]
        
