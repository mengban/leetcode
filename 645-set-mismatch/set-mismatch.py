#
# The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number. 
#
#
#
# Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.
#
#
#
# Example 1:
#
# Input: nums = [1,2,2,4]
# Output: [2,3]
#
#
#
# Note:
#
# The given array size will in the range [2, 10000].
# The given array's numbers won't have any order.
#
#


class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        #print(nums)
        length = len(nums)
        loss = None
        repeat = None
        if length ==2 :
            if nums[1]==1:# 大于2 进行判读 必须大于
                return [1,2]
            else:
                return [2,1]
        if nums[0] !=1:  #失去第一个 找不到差为2的
            loss = 1
        if nums[length-1]!=length: #失去最后一个 找不到差为2的
            loss = length
        for i in range(length):
            if i< length-1:
                if nums[i] ==nums[i+1] :
                    repeat = nums[i]
                if nums[i] == nums[i+1]-2:
                    loss = nums[i]+1
                if loss!=None and repeat !=None:
                    return[repeat,loss]
     
            
        
        
