# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note:
#
#
# 	All numbers (including target) will be positive integers.
# 	The solution set must not contain duplicate combinations.
#
#
# Example 1:
#
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
#
#
# Example 2:
#
#
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]
#
#


'''
前面的已经匹配过了 肯定不会再用了

为什么还要去重呢？因为同一个数据会多次出现。

'''
class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        for item in candidates:
            if item > target:
                candidates.remove(item)
        self.retList = []
        path = []
        for i in range(len(candidates)):
            self.findtarget(candidates[i+1:],target-candidates[i],path+[candidates[i]])
        return self.retList
    def findtarget(self,candidates,target,path):
        if target < 0 :#没有
            return None
        if target == 0:
            if sorted(path) not in self.retList:
                self.retList.append(sorted(path))
        if target in candidates:
            if sorted(path + [target]) not in self.retList:
                self.retList.append(sorted(path + [target]))
        for i in range(len(candidates)):
            self.findtarget(candidates[i+1:],target-candidates[i],path+[candidates[i]])
            
        
            
        
            
