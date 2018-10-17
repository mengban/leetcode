# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
#
# Note:
#
#
# 	Your returned answers (both index1 and index2) are not zero-based.
# 	You may assume that each input would have exactly one solution and you may not use the same element twice.
#
#
# Example:
#
#
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
#


class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not numbers:
            return 
        left = None
        ret = []
        for _  in range(len(numbers)):
            left = target - numbers[_]
            rest = numbers[_+1:]
            #print(rest)
            retInt = self.bs(rest,left) 
            if retInt!=None:
                ret.append(_+1)
                ret.append(_+retInt+2)
                return ret
                
    def bs(self,rest,tar):
        if not rest :
            return None
        if rest[-1] < tar:  # 最大值比目标值小
            return None
        start = 0
        end = len(rest)-1
        
        while(end >= start):
            mid = (start+end)//2
            #print(start,mid,end,rest[start],rest[mid],rest[end])
            if rest[mid] == tar:
                return mid
            if rest[mid]>tar: # tar [mid]  
                end =mid
            if rest[mid] <tar: # [mid] tar
                start = mid
            #print(start,mid,end,rest[start],rest[mid],rest[end])
            if (end -start ==1):
                print(rest[start],rest[end],tar)
                if rest[end] == tar:
                    #print('******************')
                    return end 
                if rest[start] == tar:
                    return start
                else:
                    return None
        
