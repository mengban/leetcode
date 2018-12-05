# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# Example:
#
#
# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
#
#


'''
思路一：加去重 时间太长了 1600ms
思路二：
'''
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==0:
            return []
        if len(nums)==1:
            return [nums]
        self.ret = []
        path = []
        for i in range(len(nums)):
            if nums[i] not in nums[:i]:
                self.retper(nums[:i]+nums[i+1:],path + [nums[i]])
        return self.ret
    def retper(self,nums,path):
        if len(nums)==1: #只有一个数了
            self.ret.append(path + [nums[0]])
        for i in range(len(nums)):
            if nums[i] not in nums[:i]:
                self.retper(nums[:i]+nums[i+1:],path + [nums[i]])
