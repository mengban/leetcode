# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note: You are not suppose to use the library's sort function for this problem.
#
# Example:
#
#
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
#
# Follow up:
#
#
# 	A rather straight forward solution is a two-pass algorithm using counting sort.
# 	First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
# 	Could you come up with a one-pass algorithm using only constant space?
#
#


class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        cnt0 = 0
        cnt1 = 0
        cnt2 = 0
        for item in nums:
            if item == 0:
                cnt0 += 1
            elif item == 1:
                cnt1 += 1
            else:
                cnt2 += 1
        for i in range(cnt0):
            nums[i] = 0
        for i in range(cnt1):
            nums[i+cnt0] = 1
        for i in range(cnt2):
            nums[i+cnt0+cnt1] = 2
            
