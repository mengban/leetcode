# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#
#


'''
思路:
1.排序
2.固定一个数 然后访问这个数以后的数 
  - 去重。a固定某个数之后去重
  b -2 0 0 2 2之类的去重
          
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        pre = None
        for i in range(len(nums) - 2 ):
            if nums[i] == pre: #上次出现过
                continue
            pre = nums[i]
            l = i + 1
            r = len(nums) - 1
            target = -nums[i]
            prel = None
            prer = None
            while l<r:
                if nums[l] + nums[r] == target: #是的 则增加该list
                    if prel == nums[l]:  #
                        l +=1
                    elif prer == nums[r]:
                        r -= 1
                    else:
                        ret.append([nums[i],nums[l],nums[r]])
                        prel = nums[l]
                        prer = nums[r]
                        l += 1
                        r -= 1
                elif nums[l] + nums[r] > target:
                    prer = nums[r]
                    r -= 1
                else:
                    prel = nums[l]
                    l += 1

        return ret
                    
                
        
        
