# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
#
# The same repeated number may be chosen from candidates unlimited number of times.
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
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
#
#
# Example 2:
#
#
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]
#
#


'''
updated:
2019-02-26:
优化算法，根据nums中无重复数据的特点 去掉去重步骤。
主要改进是将每次循环时的i值作为参数传进去 当遍历到第i个数之和 i之前的数不会再用到。
因为如果要用到 则在前面的解中肯定早已将正确解找出。
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        path = []
        self.ret = []
        index = 0
        if target in candidates:
            self.ret.append([target])
        for i in range(index,len(candidates)): #
            self.func(candidates[i:],target-candidates[i],path + [candidates[i]])
        return self.ret


    def func(self ,candidates,target,path):
        if target <=0:
            return None
        if target in candidates:
            self.ret.append(path+[target])
        for i in range(len(candidates)):
            self.func(candidates[i:],target-candidates[i],path+[candidates[i]])
        
